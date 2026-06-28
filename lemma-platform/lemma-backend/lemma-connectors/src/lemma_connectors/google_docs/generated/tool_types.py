from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, RootModel

from lemma_connectors.core.results import BinaryContentResult

from lemma_connectors.google_docs.generated.pydantic_models import BatchUpdateDocumentRequest, BatchUpdateDocumentResponse, Document

class DocsDocumentsBatchUpdateToolInput(BaseModel):
    """Input for tool `docs_documents_batch_update`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    document_id: str = Field(..., description='The ID of the document to update.')
    body: BatchUpdateDocumentRequest | None = Field(default=None, description='Request body for `docs_documents_batch_update`.')
    model_config = ConfigDict(extra='forbid')

class DocsDocumentsBatchUpdateToolOutput(BatchUpdateDocumentResponse):
    """Output for tool `docs_documents_batch_update`."""
    pass

class DocsDocumentsCreateToolInput(BaseModel):
    """Input for tool `docs_documents_create`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    body: Document | None = Field(default=None, description='Request body for `docs_documents_create`.')
    model_config = ConfigDict(extra='forbid')

class DocsDocumentsCreateToolOutput(Document):
    """Output for tool `docs_documents_create`."""
    pass

class DocsDocumentsGetToolInput(BaseModel):
    """Input for tool `docs_documents_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    document_id: str = Field(..., description='The ID of the document to retrieve.')
    suggestions_view_mode: Literal['DEFAULT_FOR_CURRENT_ACCESS', 'SUGGESTIONS_INLINE', 'PREVIEW_SUGGESTIONS_ACCEPTED', 'PREVIEW_WITHOUT_SUGGESTIONS'] | None = Field(default=None, description='The suggestions view mode to apply to the document. This allows viewing the document with all suggestions inline, accepted or rejected. If one is not specified, DEFAULT_FOR_CURRENT_ACCESS is used.')
    model_config = ConfigDict(extra='forbid')

class DocsDocumentsGetToolOutput(Document):
    """Output for tool `docs_documents_get`."""
    pass

INPUT_MODELS = {
    'docs_documents_batch_update': DocsDocumentsBatchUpdateToolInput,
    'docs_documents_create': DocsDocumentsCreateToolInput,
    'docs_documents_get': DocsDocumentsGetToolInput,
}

OUTPUT_MODELS = {
    'docs_documents_batch_update': DocsDocumentsBatchUpdateToolOutput,
    'docs_documents_create': DocsDocumentsCreateToolOutput,
    'docs_documents_get': DocsDocumentsGetToolOutput,
}
