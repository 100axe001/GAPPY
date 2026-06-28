import json
import logging
import datetime
from typing import Dict, Any, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .registry import registry
from .. import models
from ..security import encrypt_data, decrypt_data

logger = logging.getLogger("lifeos.integration_service")

async def get_user_integration(db: AsyncSession, user_id: int, name: str) -> Optional[models.UserIntegration]:
    """Fetches user integration record by name."""
    result = await db.execute(
        select(models.UserIntegration).where(
            models.UserIntegration.user_id == user_id,
            models.UserIntegration.name == name
        )
    )
    return result.scalars().first()

async def get_all_user_integrations(db: AsyncSession, user_id: int) -> List[models.UserIntegration]:
    """Fetches all user integrations."""
    result = await db.execute(
        select(models.UserIntegration).where(models.UserIntegration.user_id == user_id)
    )
    return result.scalars().all()

async def save_user_credentials(db: AsyncSession, user_id: int, name: str, token_data: dict, scopes: list):
    """Encrypts credentials and saves/updates user integration state."""
    creds_str = json.dumps(token_data)
    encrypted = encrypt_data(creds_str)
    
    integration = await get_user_integration(db, user_id, name)
    meta = {}
    if integration:
        meta = dict(integration.metadata_json or {})
    
    if "email" in token_data:
        meta["email"] = token_data["email"]

    if not integration:
        integration = models.UserIntegration(
            user_id=user_id,
            name=name,
            is_connected=True,
            scopes=scopes,
            credentials_encrypted=encrypted,
            metadata_json=meta,
            health_status="healthy",
            last_sync_at=datetime.datetime.utcnow()
        )
        db.add(integration)
    else:
        integration.is_connected = True
        integration.scopes = scopes
        integration.credentials_encrypted = encrypted
        integration.metadata_json = meta
        integration.health_status = "healthy"
        integration.error_message = None
        integration.last_sync_at = datetime.datetime.utcnow()
        
    await db.flush()
    return integration

async def disconnect_user_integration(db: AsyncSession, user_id: int, name: str) -> bool:
    """Removes user integration credentials and connection state."""
    integration = await get_user_integration(db, user_id, name)
    if integration:
        await db.delete(integration)
        await db.flush()
        return True
    return False

def get_decrypted_credentials(integration: models.UserIntegration) -> dict:
    """Decrypts credentials stored in database integration entry."""
    if not integration or not integration.credentials_encrypted:
        return {}
    try:
        decrypted = decrypt_data(integration.credentials_encrypted)
        return json.loads(decrypted)
    except Exception as e:
        logger.error(f"Failed to decrypt credentials for {integration.name}: {e}")
        return {}

async def test_integration_health(db: AsyncSession, user_id: int, name: str) -> bool:
    """Checks the health of the connection, running automatic refresh if required."""
    integration = await get_user_integration(db, user_id, name)
    if not integration or not integration.is_connected:
        return False
        
    adapter = registry.get_adapter(name)
    if not adapter:
        return False
        
    creds = get_decrypted_credentials(integration)
    if not creds:
        return False
        
    success = await adapter.test_connection(creds)
    if success:
        integration.health_status = "healthy"
        integration.error_message = None
        integration.last_sync_at = datetime.datetime.utcnow()
        await db.flush()
        return True
        
    # Attempt token refresh
    refresh_token = creds.get("refresh_token")
    if refresh_token:
        try:
            logger.info(f"Attempting to refresh expired OAuth token for {name}...")
            new_tokens = await adapter.refresh_token(refresh_token)
            for k, v in new_tokens.items():
                creds[k] = v
                
            # Test again
            success = await adapter.test_connection(creds)
            if success:
                integration.credentials_encrypted = encrypt_data(json.dumps(creds))
                integration.health_status = "healthy"
                integration.error_message = None
                integration.last_sync_at = datetime.datetime.utcnow()
                await db.flush()
                return True
        except Exception as e:
            logger.error(f"Auto-refresh failed during health check for {name}: {e}")
            
    # Mark as broken
    integration.health_status = "broken"
    integration.error_message = "Authentication expired. Please reconnect."
    await db.flush()
    return False

async def execute_integration_tool(db: AsyncSession, user_id: int, name: str, action: str, arguments: dict) -> Any:
    """Executes a tool, automatically handling access token refreshes on failures."""
    integration = await get_user_integration(db, user_id, name)
    if not integration or not integration.is_connected:
        raise ValueError(f"Integration '{name}' is not connected. Connect it first.")
        
    adapter = registry.get_adapter(name)
    if not adapter:
        raise ValueError(f"Integration adapter '{name}' not found in registry.")
        
    creds = get_decrypted_credentials(integration)
    if not creds:
        raise ValueError(f"Failed to load credentials for integration '{name}'.")
        
    try:
        return await adapter.execute_tool(action, creds, arguments)
    except Exception as api_err:
        logger.warning(f"API execution failed for {name}. Attempting token refresh...")
        refresh_token = creds.get("refresh_token")
        if refresh_token:
            try:
                new_tokens = await adapter.refresh_token(refresh_token)
                for k, v in new_tokens.items():
                    creds[k] = v
                
                # Save refreshed credentials
                integration.credentials_encrypted = encrypt_data(json.dumps(creds))
                await db.flush()
                
                # Retry
                return await adapter.execute_tool(action, creds, arguments)
            except Exception as refresh_err:
                logger.error(f"Refresh and retry execution failed for {name}: {refresh_err}")
                
        # Propagate error and mark connection as broken
        integration.health_status = "broken"
        integration.error_message = str(api_err)
        await db.flush()
        raise api_err
