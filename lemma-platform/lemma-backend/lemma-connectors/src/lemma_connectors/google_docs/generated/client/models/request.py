from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_footer_request import CreateFooterRequest
  from ..models.create_footnote_request import CreateFootnoteRequest
  from ..models.create_header_request import CreateHeaderRequest
  from ..models.create_named_range_request import CreateNamedRangeRequest
  from ..models.create_paragraph_bullets_request import CreateParagraphBulletsRequest
  from ..models.delete_content_range_request import DeleteContentRangeRequest
  from ..models.delete_footer_request import DeleteFooterRequest
  from ..models.delete_header_request import DeleteHeaderRequest
  from ..models.delete_named_range_request import DeleteNamedRangeRequest
  from ..models.delete_paragraph_bullets_request import DeleteParagraphBulletsRequest
  from ..models.delete_positioned_object_request import DeletePositionedObjectRequest
  from ..models.delete_table_column_request import DeleteTableColumnRequest
  from ..models.delete_table_row_request import DeleteTableRowRequest
  from ..models.insert_inline_image_request import InsertInlineImageRequest
  from ..models.insert_page_break_request import InsertPageBreakRequest
  from ..models.insert_section_break_request import InsertSectionBreakRequest
  from ..models.insert_table_column_request import InsertTableColumnRequest
  from ..models.insert_table_request import InsertTableRequest
  from ..models.insert_table_row_request import InsertTableRowRequest
  from ..models.insert_text_request import InsertTextRequest
  from ..models.merge_table_cells_request import MergeTableCellsRequest
  from ..models.pin_table_header_rows_request import PinTableHeaderRowsRequest
  from ..models.replace_all_text_request import ReplaceAllTextRequest
  from ..models.replace_image_request import ReplaceImageRequest
  from ..models.replace_named_range_content_request import ReplaceNamedRangeContentRequest
  from ..models.unmerge_table_cells_request import UnmergeTableCellsRequest
  from ..models.update_document_style_request import UpdateDocumentStyleRequest
  from ..models.update_paragraph_style_request import UpdateParagraphStyleRequest
  from ..models.update_section_style_request import UpdateSectionStyleRequest
  from ..models.update_table_cell_style_request import UpdateTableCellStyleRequest
  from ..models.update_table_column_properties_request import UpdateTableColumnPropertiesRequest
  from ..models.update_table_row_style_request import UpdateTableRowStyleRequest
  from ..models.update_text_style_request import UpdateTextStyleRequest





T = TypeVar("T", bound="Request")



@_attrs_define
class Request:
    """ A single update to apply to a document.

        Attributes:
            create_footer (CreateFooterRequest | Unset): Creates a Footer. The new footer is applied to the SectionStyle at
                the location of the SectionBreak if specified, otherwise it is applied to the DocumentStyle. If a footer of the
                specified type already exists, a 400 bad request error is returned.
            create_footnote (CreateFootnoteRequest | Unset): Creates a Footnote segment and inserts a new FootnoteReference
                to it at the given location. The new Footnote segment will contain a space followed by a newline character.
            create_header (CreateHeaderRequest | Unset): Creates a Header. The new header is applied to the SectionStyle at
                the location of the SectionBreak if specified, otherwise it is applied to the DocumentStyle. If a header of the
                specified type already exists, a 400 bad request error is returned.
            create_named_range (CreateNamedRangeRequest | Unset): Creates a NamedRange referencing the given range.
            create_paragraph_bullets (CreateParagraphBulletsRequest | Unset): Creates bullets for all of the paragraphs that
                overlap with the given range. The nesting level of each paragraph will be determined by counting leading tabs in
                front of each paragraph. To avoid excess space between the bullet and the corresponding paragraph, these leading
                tabs are removed by this request. This may change the indices of parts of the text. If the paragraph immediately
                before paragraphs being updated is in a list with a matching preset, the paragraphs being updated are added to
                that preceding list.
            delete_content_range (DeleteContentRangeRequest | Unset): Deletes content from the document.
            delete_footer (DeleteFooterRequest | Unset): Deletes a Footer from the document.
            delete_header (DeleteHeaderRequest | Unset): Deletes a Header from the document.
            delete_named_range (DeleteNamedRangeRequest | Unset): Deletes a NamedRange.
            delete_paragraph_bullets (DeleteParagraphBulletsRequest | Unset): Deletes bullets from all of the paragraphs
                that overlap with the given range. The nesting level of each paragraph will be visually preserved by adding
                indent to the start of the corresponding paragraph.
            delete_positioned_object (DeletePositionedObjectRequest | Unset): Deletes a PositionedObject from the document.
            delete_table_column (DeleteTableColumnRequest | Unset): Deletes a column from a table.
            delete_table_row (DeleteTableRowRequest | Unset): Deletes a row from a table.
            insert_inline_image (InsertInlineImageRequest | Unset): Inserts an InlineObject containing an image at the given
                location.
            insert_page_break (InsertPageBreakRequest | Unset): Inserts a page break followed by a newline at the specified
                location.
            insert_section_break (InsertSectionBreakRequest | Unset): Inserts a section break at the given location. A
                newline character will be inserted before the section break.
            insert_table (InsertTableRequest | Unset): Inserts a table at the specified location. A newline character will
                be inserted before the inserted table.
            insert_table_column (InsertTableColumnRequest | Unset): Inserts an empty column into a table.
            insert_table_row (InsertTableRowRequest | Unset): Inserts an empty row into a table.
            insert_text (InsertTextRequest | Unset): Inserts text at the specified location.
            merge_table_cells (MergeTableCellsRequest | Unset): Merges cells in a Table.
            pin_table_header_rows (PinTableHeaderRowsRequest | Unset): Updates the number of pinned table header rows in a
                table.
            replace_all_text (ReplaceAllTextRequest | Unset): Replaces all instances of text matching a criteria with
                replace text.
            replace_image (ReplaceImageRequest | Unset): Replaces an existing image with a new image. Replacing an image
                removes some image effects from the existing image in order to mirror the behavior of the Docs editor.
            replace_named_range_content (ReplaceNamedRangeContentRequest | Unset): Replaces the contents of the specified
                NamedRange or NamedRanges with the given replacement content. Note that an individual NamedRange may consist of
                multiple discontinuous ranges. In this case, only the content in the first range will be replaced. The other
                ranges and their content will be deleted. In cases where replacing or deleting any ranges would result in an
                invalid document structure, a 400 bad request error is returned.
            unmerge_table_cells (UnmergeTableCellsRequest | Unset): Unmerges cells in a Table.
            update_document_style (UpdateDocumentStyleRequest | Unset): Updates the DocumentStyle.
            update_paragraph_style (UpdateParagraphStyleRequest | Unset): Update the styling of all paragraphs that overlap
                with the given range.
            update_section_style (UpdateSectionStyleRequest | Unset): Updates the SectionStyle.
            update_table_cell_style (UpdateTableCellStyleRequest | Unset): Updates the style of a range of table cells.
            update_table_column_properties (UpdateTableColumnPropertiesRequest | Unset): Updates the TableColumnProperties
                of columns in a table.
            update_table_row_style (UpdateTableRowStyleRequest | Unset): Updates the TableRowStyle of rows in a table.
            update_text_style (UpdateTextStyleRequest | Unset): Update the styling of text.
     """

    create_footer: CreateFooterRequest | Unset = UNSET
    create_footnote: CreateFootnoteRequest | Unset = UNSET
    create_header: CreateHeaderRequest | Unset = UNSET
    create_named_range: CreateNamedRangeRequest | Unset = UNSET
    create_paragraph_bullets: CreateParagraphBulletsRequest | Unset = UNSET
    delete_content_range: DeleteContentRangeRequest | Unset = UNSET
    delete_footer: DeleteFooterRequest | Unset = UNSET
    delete_header: DeleteHeaderRequest | Unset = UNSET
    delete_named_range: DeleteNamedRangeRequest | Unset = UNSET
    delete_paragraph_bullets: DeleteParagraphBulletsRequest | Unset = UNSET
    delete_positioned_object: DeletePositionedObjectRequest | Unset = UNSET
    delete_table_column: DeleteTableColumnRequest | Unset = UNSET
    delete_table_row: DeleteTableRowRequest | Unset = UNSET
    insert_inline_image: InsertInlineImageRequest | Unset = UNSET
    insert_page_break: InsertPageBreakRequest | Unset = UNSET
    insert_section_break: InsertSectionBreakRequest | Unset = UNSET
    insert_table: InsertTableRequest | Unset = UNSET
    insert_table_column: InsertTableColumnRequest | Unset = UNSET
    insert_table_row: InsertTableRowRequest | Unset = UNSET
    insert_text: InsertTextRequest | Unset = UNSET
    merge_table_cells: MergeTableCellsRequest | Unset = UNSET
    pin_table_header_rows: PinTableHeaderRowsRequest | Unset = UNSET
    replace_all_text: ReplaceAllTextRequest | Unset = UNSET
    replace_image: ReplaceImageRequest | Unset = UNSET
    replace_named_range_content: ReplaceNamedRangeContentRequest | Unset = UNSET
    unmerge_table_cells: UnmergeTableCellsRequest | Unset = UNSET
    update_document_style: UpdateDocumentStyleRequest | Unset = UNSET
    update_paragraph_style: UpdateParagraphStyleRequest | Unset = UNSET
    update_section_style: UpdateSectionStyleRequest | Unset = UNSET
    update_table_cell_style: UpdateTableCellStyleRequest | Unset = UNSET
    update_table_column_properties: UpdateTableColumnPropertiesRequest | Unset = UNSET
    update_table_row_style: UpdateTableRowStyleRequest | Unset = UNSET
    update_text_style: UpdateTextStyleRequest | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_footer_request import CreateFooterRequest
        from ..models.create_footnote_request import CreateFootnoteRequest
        from ..models.create_header_request import CreateHeaderRequest
        from ..models.create_named_range_request import CreateNamedRangeRequest
        from ..models.create_paragraph_bullets_request import CreateParagraphBulletsRequest
        from ..models.delete_content_range_request import DeleteContentRangeRequest
        from ..models.delete_footer_request import DeleteFooterRequest
        from ..models.delete_header_request import DeleteHeaderRequest
        from ..models.delete_named_range_request import DeleteNamedRangeRequest
        from ..models.delete_paragraph_bullets_request import DeleteParagraphBulletsRequest
        from ..models.delete_positioned_object_request import DeletePositionedObjectRequest
        from ..models.delete_table_column_request import DeleteTableColumnRequest
        from ..models.delete_table_row_request import DeleteTableRowRequest
        from ..models.insert_inline_image_request import InsertInlineImageRequest
        from ..models.insert_page_break_request import InsertPageBreakRequest
        from ..models.insert_section_break_request import InsertSectionBreakRequest
        from ..models.insert_table_column_request import InsertTableColumnRequest
        from ..models.insert_table_request import InsertTableRequest
        from ..models.insert_table_row_request import InsertTableRowRequest
        from ..models.insert_text_request import InsertTextRequest
        from ..models.merge_table_cells_request import MergeTableCellsRequest
        from ..models.pin_table_header_rows_request import PinTableHeaderRowsRequest
        from ..models.replace_all_text_request import ReplaceAllTextRequest
        from ..models.replace_image_request import ReplaceImageRequest
        from ..models.replace_named_range_content_request import ReplaceNamedRangeContentRequest
        from ..models.unmerge_table_cells_request import UnmergeTableCellsRequest
        from ..models.update_document_style_request import UpdateDocumentStyleRequest
        from ..models.update_paragraph_style_request import UpdateParagraphStyleRequest
        from ..models.update_section_style_request import UpdateSectionStyleRequest
        from ..models.update_table_cell_style_request import UpdateTableCellStyleRequest
        from ..models.update_table_column_properties_request import UpdateTableColumnPropertiesRequest
        from ..models.update_table_row_style_request import UpdateTableRowStyleRequest
        from ..models.update_text_style_request import UpdateTextStyleRequest
        create_footer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.create_footer, Unset):
            create_footer = self.create_footer.to_dict()

        create_footnote: dict[str, Any] | Unset = UNSET
        if not isinstance(self.create_footnote, Unset):
            create_footnote = self.create_footnote.to_dict()

        create_header: dict[str, Any] | Unset = UNSET
        if not isinstance(self.create_header, Unset):
            create_header = self.create_header.to_dict()

        create_named_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.create_named_range, Unset):
            create_named_range = self.create_named_range.to_dict()

        create_paragraph_bullets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.create_paragraph_bullets, Unset):
            create_paragraph_bullets = self.create_paragraph_bullets.to_dict()

        delete_content_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete_content_range, Unset):
            delete_content_range = self.delete_content_range.to_dict()

        delete_footer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete_footer, Unset):
            delete_footer = self.delete_footer.to_dict()

        delete_header: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete_header, Unset):
            delete_header = self.delete_header.to_dict()

        delete_named_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete_named_range, Unset):
            delete_named_range = self.delete_named_range.to_dict()

        delete_paragraph_bullets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete_paragraph_bullets, Unset):
            delete_paragraph_bullets = self.delete_paragraph_bullets.to_dict()

        delete_positioned_object: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete_positioned_object, Unset):
            delete_positioned_object = self.delete_positioned_object.to_dict()

        delete_table_column: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete_table_column, Unset):
            delete_table_column = self.delete_table_column.to_dict()

        delete_table_row: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delete_table_row, Unset):
            delete_table_row = self.delete_table_row.to_dict()

        insert_inline_image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.insert_inline_image, Unset):
            insert_inline_image = self.insert_inline_image.to_dict()

        insert_page_break: dict[str, Any] | Unset = UNSET
        if not isinstance(self.insert_page_break, Unset):
            insert_page_break = self.insert_page_break.to_dict()

        insert_section_break: dict[str, Any] | Unset = UNSET
        if not isinstance(self.insert_section_break, Unset):
            insert_section_break = self.insert_section_break.to_dict()

        insert_table: dict[str, Any] | Unset = UNSET
        if not isinstance(self.insert_table, Unset):
            insert_table = self.insert_table.to_dict()

        insert_table_column: dict[str, Any] | Unset = UNSET
        if not isinstance(self.insert_table_column, Unset):
            insert_table_column = self.insert_table_column.to_dict()

        insert_table_row: dict[str, Any] | Unset = UNSET
        if not isinstance(self.insert_table_row, Unset):
            insert_table_row = self.insert_table_row.to_dict()

        insert_text: dict[str, Any] | Unset = UNSET
        if not isinstance(self.insert_text, Unset):
            insert_text = self.insert_text.to_dict()

        merge_table_cells: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merge_table_cells, Unset):
            merge_table_cells = self.merge_table_cells.to_dict()

        pin_table_header_rows: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pin_table_header_rows, Unset):
            pin_table_header_rows = self.pin_table_header_rows.to_dict()

        replace_all_text: dict[str, Any] | Unset = UNSET
        if not isinstance(self.replace_all_text, Unset):
            replace_all_text = self.replace_all_text.to_dict()

        replace_image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.replace_image, Unset):
            replace_image = self.replace_image.to_dict()

        replace_named_range_content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.replace_named_range_content, Unset):
            replace_named_range_content = self.replace_named_range_content.to_dict()

        unmerge_table_cells: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unmerge_table_cells, Unset):
            unmerge_table_cells = self.unmerge_table_cells.to_dict()

        update_document_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_document_style, Unset):
            update_document_style = self.update_document_style.to_dict()

        update_paragraph_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_paragraph_style, Unset):
            update_paragraph_style = self.update_paragraph_style.to_dict()

        update_section_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_section_style, Unset):
            update_section_style = self.update_section_style.to_dict()

        update_table_cell_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_table_cell_style, Unset):
            update_table_cell_style = self.update_table_cell_style.to_dict()

        update_table_column_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_table_column_properties, Unset):
            update_table_column_properties = self.update_table_column_properties.to_dict()

        update_table_row_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_table_row_style, Unset):
            update_table_row_style = self.update_table_row_style.to_dict()

        update_text_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_text_style, Unset):
            update_text_style = self.update_text_style.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if create_footer is not UNSET:
            field_dict["createFooter"] = create_footer
        if create_footnote is not UNSET:
            field_dict["createFootnote"] = create_footnote
        if create_header is not UNSET:
            field_dict["createHeader"] = create_header
        if create_named_range is not UNSET:
            field_dict["createNamedRange"] = create_named_range
        if create_paragraph_bullets is not UNSET:
            field_dict["createParagraphBullets"] = create_paragraph_bullets
        if delete_content_range is not UNSET:
            field_dict["deleteContentRange"] = delete_content_range
        if delete_footer is not UNSET:
            field_dict["deleteFooter"] = delete_footer
        if delete_header is not UNSET:
            field_dict["deleteHeader"] = delete_header
        if delete_named_range is not UNSET:
            field_dict["deleteNamedRange"] = delete_named_range
        if delete_paragraph_bullets is not UNSET:
            field_dict["deleteParagraphBullets"] = delete_paragraph_bullets
        if delete_positioned_object is not UNSET:
            field_dict["deletePositionedObject"] = delete_positioned_object
        if delete_table_column is not UNSET:
            field_dict["deleteTableColumn"] = delete_table_column
        if delete_table_row is not UNSET:
            field_dict["deleteTableRow"] = delete_table_row
        if insert_inline_image is not UNSET:
            field_dict["insertInlineImage"] = insert_inline_image
        if insert_page_break is not UNSET:
            field_dict["insertPageBreak"] = insert_page_break
        if insert_section_break is not UNSET:
            field_dict["insertSectionBreak"] = insert_section_break
        if insert_table is not UNSET:
            field_dict["insertTable"] = insert_table
        if insert_table_column is not UNSET:
            field_dict["insertTableColumn"] = insert_table_column
        if insert_table_row is not UNSET:
            field_dict["insertTableRow"] = insert_table_row
        if insert_text is not UNSET:
            field_dict["insertText"] = insert_text
        if merge_table_cells is not UNSET:
            field_dict["mergeTableCells"] = merge_table_cells
        if pin_table_header_rows is not UNSET:
            field_dict["pinTableHeaderRows"] = pin_table_header_rows
        if replace_all_text is not UNSET:
            field_dict["replaceAllText"] = replace_all_text
        if replace_image is not UNSET:
            field_dict["replaceImage"] = replace_image
        if replace_named_range_content is not UNSET:
            field_dict["replaceNamedRangeContent"] = replace_named_range_content
        if unmerge_table_cells is not UNSET:
            field_dict["unmergeTableCells"] = unmerge_table_cells
        if update_document_style is not UNSET:
            field_dict["updateDocumentStyle"] = update_document_style
        if update_paragraph_style is not UNSET:
            field_dict["updateParagraphStyle"] = update_paragraph_style
        if update_section_style is not UNSET:
            field_dict["updateSectionStyle"] = update_section_style
        if update_table_cell_style is not UNSET:
            field_dict["updateTableCellStyle"] = update_table_cell_style
        if update_table_column_properties is not UNSET:
            field_dict["updateTableColumnProperties"] = update_table_column_properties
        if update_table_row_style is not UNSET:
            field_dict["updateTableRowStyle"] = update_table_row_style
        if update_text_style is not UNSET:
            field_dict["updateTextStyle"] = update_text_style

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_footer_request import CreateFooterRequest
        from ..models.create_footnote_request import CreateFootnoteRequest
        from ..models.create_header_request import CreateHeaderRequest
        from ..models.create_named_range_request import CreateNamedRangeRequest
        from ..models.create_paragraph_bullets_request import CreateParagraphBulletsRequest
        from ..models.delete_content_range_request import DeleteContentRangeRequest
        from ..models.delete_footer_request import DeleteFooterRequest
        from ..models.delete_header_request import DeleteHeaderRequest
        from ..models.delete_named_range_request import DeleteNamedRangeRequest
        from ..models.delete_paragraph_bullets_request import DeleteParagraphBulletsRequest
        from ..models.delete_positioned_object_request import DeletePositionedObjectRequest
        from ..models.delete_table_column_request import DeleteTableColumnRequest
        from ..models.delete_table_row_request import DeleteTableRowRequest
        from ..models.insert_inline_image_request import InsertInlineImageRequest
        from ..models.insert_page_break_request import InsertPageBreakRequest
        from ..models.insert_section_break_request import InsertSectionBreakRequest
        from ..models.insert_table_column_request import InsertTableColumnRequest
        from ..models.insert_table_request import InsertTableRequest
        from ..models.insert_table_row_request import InsertTableRowRequest
        from ..models.insert_text_request import InsertTextRequest
        from ..models.merge_table_cells_request import MergeTableCellsRequest
        from ..models.pin_table_header_rows_request import PinTableHeaderRowsRequest
        from ..models.replace_all_text_request import ReplaceAllTextRequest
        from ..models.replace_image_request import ReplaceImageRequest
        from ..models.replace_named_range_content_request import ReplaceNamedRangeContentRequest
        from ..models.unmerge_table_cells_request import UnmergeTableCellsRequest
        from ..models.update_document_style_request import UpdateDocumentStyleRequest
        from ..models.update_paragraph_style_request import UpdateParagraphStyleRequest
        from ..models.update_section_style_request import UpdateSectionStyleRequest
        from ..models.update_table_cell_style_request import UpdateTableCellStyleRequest
        from ..models.update_table_column_properties_request import UpdateTableColumnPropertiesRequest
        from ..models.update_table_row_style_request import UpdateTableRowStyleRequest
        from ..models.update_text_style_request import UpdateTextStyleRequest
        d = dict(src_dict)
        _create_footer = d.pop("createFooter", UNSET)
        create_footer: CreateFooterRequest | Unset
        if isinstance(_create_footer,  Unset):
            create_footer = UNSET
        else:
            create_footer = CreateFooterRequest.from_dict(_create_footer)




        _create_footnote = d.pop("createFootnote", UNSET)
        create_footnote: CreateFootnoteRequest | Unset
        if isinstance(_create_footnote,  Unset):
            create_footnote = UNSET
        else:
            create_footnote = CreateFootnoteRequest.from_dict(_create_footnote)




        _create_header = d.pop("createHeader", UNSET)
        create_header: CreateHeaderRequest | Unset
        if isinstance(_create_header,  Unset):
            create_header = UNSET
        else:
            create_header = CreateHeaderRequest.from_dict(_create_header)




        _create_named_range = d.pop("createNamedRange", UNSET)
        create_named_range: CreateNamedRangeRequest | Unset
        if isinstance(_create_named_range,  Unset):
            create_named_range = UNSET
        else:
            create_named_range = CreateNamedRangeRequest.from_dict(_create_named_range)




        _create_paragraph_bullets = d.pop("createParagraphBullets", UNSET)
        create_paragraph_bullets: CreateParagraphBulletsRequest | Unset
        if isinstance(_create_paragraph_bullets,  Unset):
            create_paragraph_bullets = UNSET
        else:
            create_paragraph_bullets = CreateParagraphBulletsRequest.from_dict(_create_paragraph_bullets)




        _delete_content_range = d.pop("deleteContentRange", UNSET)
        delete_content_range: DeleteContentRangeRequest | Unset
        if isinstance(_delete_content_range,  Unset):
            delete_content_range = UNSET
        else:
            delete_content_range = DeleteContentRangeRequest.from_dict(_delete_content_range)




        _delete_footer = d.pop("deleteFooter", UNSET)
        delete_footer: DeleteFooterRequest | Unset
        if isinstance(_delete_footer,  Unset):
            delete_footer = UNSET
        else:
            delete_footer = DeleteFooterRequest.from_dict(_delete_footer)




        _delete_header = d.pop("deleteHeader", UNSET)
        delete_header: DeleteHeaderRequest | Unset
        if isinstance(_delete_header,  Unset):
            delete_header = UNSET
        else:
            delete_header = DeleteHeaderRequest.from_dict(_delete_header)




        _delete_named_range = d.pop("deleteNamedRange", UNSET)
        delete_named_range: DeleteNamedRangeRequest | Unset
        if isinstance(_delete_named_range,  Unset):
            delete_named_range = UNSET
        else:
            delete_named_range = DeleteNamedRangeRequest.from_dict(_delete_named_range)




        _delete_paragraph_bullets = d.pop("deleteParagraphBullets", UNSET)
        delete_paragraph_bullets: DeleteParagraphBulletsRequest | Unset
        if isinstance(_delete_paragraph_bullets,  Unset):
            delete_paragraph_bullets = UNSET
        else:
            delete_paragraph_bullets = DeleteParagraphBulletsRequest.from_dict(_delete_paragraph_bullets)




        _delete_positioned_object = d.pop("deletePositionedObject", UNSET)
        delete_positioned_object: DeletePositionedObjectRequest | Unset
        if isinstance(_delete_positioned_object,  Unset):
            delete_positioned_object = UNSET
        else:
            delete_positioned_object = DeletePositionedObjectRequest.from_dict(_delete_positioned_object)




        _delete_table_column = d.pop("deleteTableColumn", UNSET)
        delete_table_column: DeleteTableColumnRequest | Unset
        if isinstance(_delete_table_column,  Unset):
            delete_table_column = UNSET
        else:
            delete_table_column = DeleteTableColumnRequest.from_dict(_delete_table_column)




        _delete_table_row = d.pop("deleteTableRow", UNSET)
        delete_table_row: DeleteTableRowRequest | Unset
        if isinstance(_delete_table_row,  Unset):
            delete_table_row = UNSET
        else:
            delete_table_row = DeleteTableRowRequest.from_dict(_delete_table_row)




        _insert_inline_image = d.pop("insertInlineImage", UNSET)
        insert_inline_image: InsertInlineImageRequest | Unset
        if isinstance(_insert_inline_image,  Unset):
            insert_inline_image = UNSET
        else:
            insert_inline_image = InsertInlineImageRequest.from_dict(_insert_inline_image)




        _insert_page_break = d.pop("insertPageBreak", UNSET)
        insert_page_break: InsertPageBreakRequest | Unset
        if isinstance(_insert_page_break,  Unset):
            insert_page_break = UNSET
        else:
            insert_page_break = InsertPageBreakRequest.from_dict(_insert_page_break)




        _insert_section_break = d.pop("insertSectionBreak", UNSET)
        insert_section_break: InsertSectionBreakRequest | Unset
        if isinstance(_insert_section_break,  Unset):
            insert_section_break = UNSET
        else:
            insert_section_break = InsertSectionBreakRequest.from_dict(_insert_section_break)




        _insert_table = d.pop("insertTable", UNSET)
        insert_table: InsertTableRequest | Unset
        if isinstance(_insert_table,  Unset):
            insert_table = UNSET
        else:
            insert_table = InsertTableRequest.from_dict(_insert_table)




        _insert_table_column = d.pop("insertTableColumn", UNSET)
        insert_table_column: InsertTableColumnRequest | Unset
        if isinstance(_insert_table_column,  Unset):
            insert_table_column = UNSET
        else:
            insert_table_column = InsertTableColumnRequest.from_dict(_insert_table_column)




        _insert_table_row = d.pop("insertTableRow", UNSET)
        insert_table_row: InsertTableRowRequest | Unset
        if isinstance(_insert_table_row,  Unset):
            insert_table_row = UNSET
        else:
            insert_table_row = InsertTableRowRequest.from_dict(_insert_table_row)




        _insert_text = d.pop("insertText", UNSET)
        insert_text: InsertTextRequest | Unset
        if isinstance(_insert_text,  Unset):
            insert_text = UNSET
        else:
            insert_text = InsertTextRequest.from_dict(_insert_text)




        _merge_table_cells = d.pop("mergeTableCells", UNSET)
        merge_table_cells: MergeTableCellsRequest | Unset
        if isinstance(_merge_table_cells,  Unset):
            merge_table_cells = UNSET
        else:
            merge_table_cells = MergeTableCellsRequest.from_dict(_merge_table_cells)




        _pin_table_header_rows = d.pop("pinTableHeaderRows", UNSET)
        pin_table_header_rows: PinTableHeaderRowsRequest | Unset
        if isinstance(_pin_table_header_rows,  Unset):
            pin_table_header_rows = UNSET
        else:
            pin_table_header_rows = PinTableHeaderRowsRequest.from_dict(_pin_table_header_rows)




        _replace_all_text = d.pop("replaceAllText", UNSET)
        replace_all_text: ReplaceAllTextRequest | Unset
        if isinstance(_replace_all_text,  Unset):
            replace_all_text = UNSET
        else:
            replace_all_text = ReplaceAllTextRequest.from_dict(_replace_all_text)




        _replace_image = d.pop("replaceImage", UNSET)
        replace_image: ReplaceImageRequest | Unset
        if isinstance(_replace_image,  Unset):
            replace_image = UNSET
        else:
            replace_image = ReplaceImageRequest.from_dict(_replace_image)




        _replace_named_range_content = d.pop("replaceNamedRangeContent", UNSET)
        replace_named_range_content: ReplaceNamedRangeContentRequest | Unset
        if isinstance(_replace_named_range_content,  Unset):
            replace_named_range_content = UNSET
        else:
            replace_named_range_content = ReplaceNamedRangeContentRequest.from_dict(_replace_named_range_content)




        _unmerge_table_cells = d.pop("unmergeTableCells", UNSET)
        unmerge_table_cells: UnmergeTableCellsRequest | Unset
        if isinstance(_unmerge_table_cells,  Unset):
            unmerge_table_cells = UNSET
        else:
            unmerge_table_cells = UnmergeTableCellsRequest.from_dict(_unmerge_table_cells)




        _update_document_style = d.pop("updateDocumentStyle", UNSET)
        update_document_style: UpdateDocumentStyleRequest | Unset
        if isinstance(_update_document_style,  Unset):
            update_document_style = UNSET
        else:
            update_document_style = UpdateDocumentStyleRequest.from_dict(_update_document_style)




        _update_paragraph_style = d.pop("updateParagraphStyle", UNSET)
        update_paragraph_style: UpdateParagraphStyleRequest | Unset
        if isinstance(_update_paragraph_style,  Unset):
            update_paragraph_style = UNSET
        else:
            update_paragraph_style = UpdateParagraphStyleRequest.from_dict(_update_paragraph_style)




        _update_section_style = d.pop("updateSectionStyle", UNSET)
        update_section_style: UpdateSectionStyleRequest | Unset
        if isinstance(_update_section_style,  Unset):
            update_section_style = UNSET
        else:
            update_section_style = UpdateSectionStyleRequest.from_dict(_update_section_style)




        _update_table_cell_style = d.pop("updateTableCellStyle", UNSET)
        update_table_cell_style: UpdateTableCellStyleRequest | Unset
        if isinstance(_update_table_cell_style,  Unset):
            update_table_cell_style = UNSET
        else:
            update_table_cell_style = UpdateTableCellStyleRequest.from_dict(_update_table_cell_style)




        _update_table_column_properties = d.pop("updateTableColumnProperties", UNSET)
        update_table_column_properties: UpdateTableColumnPropertiesRequest | Unset
        if isinstance(_update_table_column_properties,  Unset):
            update_table_column_properties = UNSET
        else:
            update_table_column_properties = UpdateTableColumnPropertiesRequest.from_dict(_update_table_column_properties)




        _update_table_row_style = d.pop("updateTableRowStyle", UNSET)
        update_table_row_style: UpdateTableRowStyleRequest | Unset
        if isinstance(_update_table_row_style,  Unset):
            update_table_row_style = UNSET
        else:
            update_table_row_style = UpdateTableRowStyleRequest.from_dict(_update_table_row_style)




        _update_text_style = d.pop("updateTextStyle", UNSET)
        update_text_style: UpdateTextStyleRequest | Unset
        if isinstance(_update_text_style,  Unset):
            update_text_style = UNSET
        else:
            update_text_style = UpdateTextStyleRequest.from_dict(_update_text_style)




        request = cls(
            create_footer=create_footer,
            create_footnote=create_footnote,
            create_header=create_header,
            create_named_range=create_named_range,
            create_paragraph_bullets=create_paragraph_bullets,
            delete_content_range=delete_content_range,
            delete_footer=delete_footer,
            delete_header=delete_header,
            delete_named_range=delete_named_range,
            delete_paragraph_bullets=delete_paragraph_bullets,
            delete_positioned_object=delete_positioned_object,
            delete_table_column=delete_table_column,
            delete_table_row=delete_table_row,
            insert_inline_image=insert_inline_image,
            insert_page_break=insert_page_break,
            insert_section_break=insert_section_break,
            insert_table=insert_table,
            insert_table_column=insert_table_column,
            insert_table_row=insert_table_row,
            insert_text=insert_text,
            merge_table_cells=merge_table_cells,
            pin_table_header_rows=pin_table_header_rows,
            replace_all_text=replace_all_text,
            replace_image=replace_image,
            replace_named_range_content=replace_named_range_content,
            unmerge_table_cells=unmerge_table_cells,
            update_document_style=update_document_style,
            update_paragraph_style=update_paragraph_style,
            update_section_style=update_section_style,
            update_table_cell_style=update_table_cell_style,
            update_table_column_properties=update_table_column_properties,
            update_table_row_style=update_table_row_style,
            update_text_style=update_text_style,
        )


        request.additional_properties = d
        return request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
