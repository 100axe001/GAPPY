import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete
from . import models, schemas
from . import pod_store

# ---------------------------------------------------------------------------
# Items, connections, and study reviews now live in the Lemma pod datastore
# (see pod_store.py). These thin wrappers keep the crud.* call sites in main.py
# unchanged; the `db` argument is accepted for signature compatibility and is
# unused for these pod-backed entities. Users, settings, and chat stay on Postgres.
# ---------------------------------------------------------------------------

# -- User Helpers --
async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(models.User).where(models.User.email == email))
    return result.scalars().first()

async def create_user(db: AsyncSession, user_in: schemas.UserCreate, hashed_password: str):
    db_user = models.User(email=user_in.email, hashed_password=hashed_password)
    db.add(db_user)
    await db.flush()
    return db_user

# -- Item Helpers (pod-backed) --
async def get_item(db: AsyncSession, item_id):
    return await pod_store.get_item(item_id)

async def get_items(db: AsyncSession, skip: int = 0, limit: int = 500, item_type: str = None):
    return await pod_store.get_items(item_type=item_type, limit=limit)

async def create_item(db: AsyncSession, item_in: schemas.ItemCreate):
    return await pod_store.create_item(item_in)

async def update_item(db: AsyncSession, item_id, item_in: schemas.ItemUpdate):
    return await pod_store.update_item(item_id, item_in)

async def delete_item(db: AsyncSession, item_id):
    return await pod_store.delete_item(item_id)

# -- Connection Helpers (pod-backed) --
async def create_connection(db: AsyncSession, conn_in: schemas.ConnectionCreate):
    return await pod_store.create_connection(conn_in)

async def get_connections(db: AsyncSession, skip: int = 0, limit: int = 200):
    return await pod_store.get_connections(limit=limit)

async def get_connections_by_item_id(db: AsyncSession, item_id):
    return await pod_store.get_connections_by_item_id(item_id)

async def delete_connection(db: AsyncSession, connection_id):
    return await pod_store.delete_connection(connection_id)

# -- Conversation / Message Helpers --
async def create_conversation(db: AsyncSession, user_id: int, title: str = "New Chat", tag: str = None):
    conv = models.Conversation(user_id=user_id, title=title or "New Chat", tag=tag, metadata_json={})
    db.add(conv)
    await db.flush()
    return conv

async def get_conversation(db: AsyncSession, conv_id: int, user_id: int):
    result = await db.execute(
        select(models.Conversation).where(
            models.Conversation.id == conv_id,
            models.Conversation.user_id == user_id
        )
    )
    return result.scalars().first()

async def list_conversations(db: AsyncSession, user_id: int):
    result = await db.execute(
        select(models.Conversation)
        .where(models.Conversation.user_id == user_id)
        .order_by(models.Conversation.updated_at.desc())
    )
    return result.scalars().all()

async def update_conversation(db: AsyncSession, conv_id: int, user_id: int, **fields):
    conv = await get_conversation(db, conv_id, user_id)
    if not conv:
        return None
    for key, value in fields.items():
        if value is not None:
            setattr(conv, key, value)
    await db.flush()
    return conv

async def touch_conversation(db: AsyncSession, conv: models.Conversation):
    conv.updated_at = datetime.datetime.utcnow()
    await db.flush()

async def delete_conversation(db: AsyncSession, conv_id: int, user_id: int):
    conv = await get_conversation(db, conv_id, user_id)
    if not conv:
        return False
    await db.delete(conv)
    await db.flush()
    return True

async def add_message(db: AsyncSession, conversation_id: int, role: str, content: str,
                      tool_calls=None, metadata=None):
    msg = models.Message(
        conversation_id=conversation_id,
        role=role,
        content=content,
        tool_calls_json=tool_calls or [],
        metadata_json=metadata or {}
    )
    db.add(msg)
    await db.flush()
    return msg

async def get_messages(db: AsyncSession, conversation_id: int):
    result = await db.execute(
        select(models.Message)
        .where(models.Message.conversation_id == conversation_id)
        .order_by(models.Message.created_at.asc(), models.Message.id.asc())
    )
    return result.scalars().all()

# -- Settings Helpers --
async def get_setting_row(db: AsyncSession, user_id: int, key: str):
    result = await db.execute(
        select(models.UserSetting).where(
            models.UserSetting.user_id == user_id,
            models.UserSetting.key == key
        )
    )
    return result.scalars().first()

async def get_all_settings(db: AsyncSession, user_id: int):
    result = await db.execute(
        select(models.UserSetting).where(models.UserSetting.user_id == user_id)
    )
    return result.scalars().all()

async def upsert_setting(db: AsyncSession, user_id: int, key: str, value: str, is_secret: bool = False):
    row = await get_setting_row(db, user_id, key)
    if row:
        row.value = value
        row.is_secret = is_secret
    else:
        row = models.UserSetting(user_id=user_id, key=key, value=value, is_secret=is_secret)
        db.add(row)
    await db.flush()
    return row

# -- StudyReview Helpers (Spaced Repetition, pod-backed) --
async def get_study_review_by_concept(db: AsyncSession, concept_id, user_id=None):
    return await pod_store.get_study_review_by_concept(concept_id)

async def create_study_review(db: AsyncSession, concept_id, user_id=None, concept_title: str = ""):
    return await pod_store.create_study_review(concept_id, concept_title=concept_title)

async def get_due_study_reviews(db: AsyncSession, user_id=None):
    return await pod_store.get_due_study_reviews()

async def update_study_review(db: AsyncSession, review_id, score: int):
    return await pod_store.update_study_review(review_id, score)

