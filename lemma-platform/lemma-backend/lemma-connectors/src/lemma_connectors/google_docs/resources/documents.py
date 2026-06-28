from __future__ import annotations

from lemma_connectors.google_docs.generated.tool_types import DocsDocumentsBatchUpdateToolInput, DocsDocumentsBatchUpdateToolOutput, DocsDocumentsCreateToolInput, DocsDocumentsCreateToolOutput, DocsDocumentsGetToolInput, DocsDocumentsGetToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DocumentsBatchUpdateInput(DocsDocumentsBatchUpdateToolInput):
    """Operation input for `documents_batch_update`."""
    pass

class DocumentsBatchUpdateOutput(DocsDocumentsBatchUpdateToolOutput):
    """Operation output for `documents_batch_update`."""
    pass

class DocumentsCreateInput(DocsDocumentsCreateToolInput):
    """Operation input for `documents_create`."""
    pass

class DocumentsCreateOutput(DocsDocumentsCreateToolOutput):
    """Operation output for `documents_create`."""
    pass

class DocumentsGetInput(DocsDocumentsGetToolInput):
    """Operation input for `documents_get`."""
    pass

class DocumentsGetOutput(DocsDocumentsGetToolOutput):
    """Operation output for `documents_get`."""
    pass

class GoogleDocsDocumentsResource(BaseResourceClient):
    """Operations for the `documents` resource."""

    @operation(
        name='documents_batch_update',
        title='DocumentsBatchUpdate',
        input_model=DocumentsBatchUpdateInput,
        output_model=DocumentsBatchUpdateOutput,
        tools_used=('docs_documents_batch_update',),
        tags=tuple(['documents']),
    )
    async def batch_update(self, data: DocumentsBatchUpdateInput) -> DocumentsBatchUpdateOutput:
        """Applies one or more updates to the document. Each request is validated before being applied. If any request is not valid, then the entire request will fail and nothing will be applied. Some requests have replies to give you some information about how they are applied. Other requests do not need to return information; these each return an empty reply. The order of replies matches that of the requests. For example, suppose you call batchUpdate with four updates, and only the third one returns information. The response would have two empty replies, the reply to the third request, and another empty reply, in that order. Because other users may be editing the document, the document might not exactly reflect your changes: your changes may be altered with respect to collaborator changes. If there are no collaborators, the document should reflect your changes. In any case, the updates in your request are guaranteed to be applied together atomically.

Important inputs: fields, document_id, body"""
        tool = self._client.get_tool('docs_documents_batch_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DocumentsBatchUpdateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='documents_create',
        title='DocumentsCreate',
        input_model=DocumentsCreateInput,
        output_model=DocumentsCreateOutput,
        tools_used=('docs_documents_create',),
        tags=tuple(['documents']),
    )
    async def create(self, data: DocumentsCreateInput) -> DocumentsCreateOutput:
        """Creates a blank document using the title given in the request. Other fields in the request, including any provided content, are ignored. Returns the created document.

Important inputs: fields, body"""
        tool = self._client.get_tool('docs_documents_create')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DocumentsCreateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='documents_get',
        title='DocumentsGet',
        input_model=DocumentsGetInput,
        output_model=DocumentsGetOutput,
        tools_used=('docs_documents_get',),
        tags=tuple(['documents']),
    )
    async def get(self, data: DocumentsGetInput) -> DocumentsGetOutput:
        """Gets the latest version of the specified document.

Important inputs: fields, document_id, suggestions_view_mode"""
        tool = self._client.get_tool('docs_documents_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DocumentsGetOutput.model_validate(coerce_tool_result(result))
