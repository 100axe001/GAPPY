from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.included_fields import IncludedFields
  from ..models.issue_bean_fields import IssueBeanFields
  from ..models.issue_bean_names import IssueBeanNames
  from ..models.issue_bean_properties import IssueBeanProperties
  from ..models.issue_bean_rendered_fields import IssueBeanRenderedFields
  from ..models.issue_bean_schema import IssueBeanSchema
  from ..models.issue_bean_versioned_representations import IssueBeanVersionedRepresentations
  from ..models.issue_transition import IssueTransition
  from ..models.issue_update_metadata import IssueUpdateMetadata
  from ..models.operations import Operations
  from ..models.page_of_changelogs import PageOfChangelogs





T = TypeVar("T", bound="IssueBean")



@_attrs_define
class IssueBean:
    """ Details about an issue.

        Attributes:
            changelog (PageOfChangelogs | Unset): A page of changelogs.
            editmeta (IssueUpdateMetadata | Unset): A list of editable field details.
            expand (str | Unset): Expand options that include additional issue details in the response.
            fields (IssueBeanFields | Unset):
            fields_to_include (IncludedFields | Unset):
            id (str | Unset): The ID of the issue.
            key (str | Unset): The key of the issue.
            names (IssueBeanNames | Unset): The ID and name of each field present on the issue.
            operations (Operations | Unset): Details of the operations that can be performed on the issue.
            properties (IssueBeanProperties | Unset): Details of the issue properties identified in the request.
            rendered_fields (IssueBeanRenderedFields | Unset): The rendered value of each field present on the issue.
            schema (IssueBeanSchema | Unset): The schema describing each field present on the issue.
            self_ (str | Unset): The URL of the issue details.
            transitions (list[IssueTransition] | Unset): The transitions that can be performed on the issue.
            versioned_representations (IssueBeanVersionedRepresentations | Unset): The versions of each field on the issue.
     """

    changelog: PageOfChangelogs | Unset = UNSET
    editmeta: IssueUpdateMetadata | Unset = UNSET
    expand: str | Unset = UNSET
    fields: IssueBeanFields | Unset = UNSET
    fields_to_include: IncludedFields | Unset = UNSET
    id: str | Unset = UNSET
    key: str | Unset = UNSET
    names: IssueBeanNames | Unset = UNSET
    operations: Operations | Unset = UNSET
    properties: IssueBeanProperties | Unset = UNSET
    rendered_fields: IssueBeanRenderedFields | Unset = UNSET
    schema: IssueBeanSchema | Unset = UNSET
    self_: str | Unset = UNSET
    transitions: list[IssueTransition] | Unset = UNSET
    versioned_representations: IssueBeanVersionedRepresentations | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.included_fields import IncludedFields
        from ..models.issue_bean_fields import IssueBeanFields
        from ..models.issue_bean_names import IssueBeanNames
        from ..models.issue_bean_properties import IssueBeanProperties
        from ..models.issue_bean_rendered_fields import IssueBeanRenderedFields
        from ..models.issue_bean_schema import IssueBeanSchema
        from ..models.issue_bean_versioned_representations import IssueBeanVersionedRepresentations
        from ..models.issue_transition import IssueTransition
        from ..models.issue_update_metadata import IssueUpdateMetadata
        from ..models.operations import Operations
        from ..models.page_of_changelogs import PageOfChangelogs
        changelog: dict[str, Any] | Unset = UNSET
        if not isinstance(self.changelog, Unset):
            changelog = self.changelog.to_dict()

        editmeta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.editmeta, Unset):
            editmeta = self.editmeta.to_dict()

        expand = self.expand

        fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()

        fields_to_include: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fields_to_include, Unset):
            fields_to_include = self.fields_to_include.to_dict()

        id = self.id

        key = self.key

        names: dict[str, Any] | Unset = UNSET
        if not isinstance(self.names, Unset):
            names = self.names.to_dict()

        operations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.operations, Unset):
            operations = self.operations.to_dict()

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        rendered_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rendered_fields, Unset):
            rendered_fields = self.rendered_fields.to_dict()

        schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schema, Unset):
            schema = self.schema.to_dict()

        self_ = self.self_

        transitions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.transitions, Unset):
            transitions = []
            for transitions_item_data in self.transitions:
                transitions_item = transitions_item_data.to_dict()
                transitions.append(transitions_item)



        versioned_representations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.versioned_representations, Unset):
            versioned_representations = self.versioned_representations.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if changelog is not UNSET:
            field_dict["changelog"] = changelog
        if editmeta is not UNSET:
            field_dict["editmeta"] = editmeta
        if expand is not UNSET:
            field_dict["expand"] = expand
        if fields is not UNSET:
            field_dict["fields"] = fields
        if fields_to_include is not UNSET:
            field_dict["fieldsToInclude"] = fields_to_include
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if names is not UNSET:
            field_dict["names"] = names
        if operations is not UNSET:
            field_dict["operations"] = operations
        if properties is not UNSET:
            field_dict["properties"] = properties
        if rendered_fields is not UNSET:
            field_dict["renderedFields"] = rendered_fields
        if schema is not UNSET:
            field_dict["schema"] = schema
        if self_ is not UNSET:
            field_dict["self"] = self_
        if transitions is not UNSET:
            field_dict["transitions"] = transitions
        if versioned_representations is not UNSET:
            field_dict["versionedRepresentations"] = versioned_representations

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.included_fields import IncludedFields
        from ..models.issue_bean_fields import IssueBeanFields
        from ..models.issue_bean_names import IssueBeanNames
        from ..models.issue_bean_properties import IssueBeanProperties
        from ..models.issue_bean_rendered_fields import IssueBeanRenderedFields
        from ..models.issue_bean_schema import IssueBeanSchema
        from ..models.issue_bean_versioned_representations import IssueBeanVersionedRepresentations
        from ..models.issue_transition import IssueTransition
        from ..models.issue_update_metadata import IssueUpdateMetadata
        from ..models.operations import Operations
        from ..models.page_of_changelogs import PageOfChangelogs
        d = dict(src_dict)
        _changelog = d.pop("changelog", UNSET)
        changelog: PageOfChangelogs | Unset
        if isinstance(_changelog,  Unset):
            changelog = UNSET
        else:
            changelog = PageOfChangelogs.from_dict(_changelog)




        _editmeta = d.pop("editmeta", UNSET)
        editmeta: IssueUpdateMetadata | Unset
        if isinstance(_editmeta,  Unset):
            editmeta = UNSET
        else:
            editmeta = IssueUpdateMetadata.from_dict(_editmeta)




        expand = d.pop("expand", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: IssueBeanFields | Unset
        if isinstance(_fields,  Unset):
            fields = UNSET
        else:
            fields = IssueBeanFields.from_dict(_fields)




        _fields_to_include = d.pop("fieldsToInclude", UNSET)
        fields_to_include: IncludedFields | Unset
        if isinstance(_fields_to_include,  Unset):
            fields_to_include = UNSET
        else:
            fields_to_include = IncludedFields.from_dict(_fields_to_include)




        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        _names = d.pop("names", UNSET)
        names: IssueBeanNames | Unset
        if isinstance(_names,  Unset):
            names = UNSET
        else:
            names = IssueBeanNames.from_dict(_names)




        _operations = d.pop("operations", UNSET)
        operations: Operations | Unset
        if isinstance(_operations,  Unset):
            operations = UNSET
        else:
            operations = Operations.from_dict(_operations)




        _properties = d.pop("properties", UNSET)
        properties: IssueBeanProperties | Unset
        if isinstance(_properties,  Unset):
            properties = UNSET
        else:
            properties = IssueBeanProperties.from_dict(_properties)




        _rendered_fields = d.pop("renderedFields", UNSET)
        rendered_fields: IssueBeanRenderedFields | Unset
        if isinstance(_rendered_fields,  Unset):
            rendered_fields = UNSET
        else:
            rendered_fields = IssueBeanRenderedFields.from_dict(_rendered_fields)




        _schema = d.pop("schema", UNSET)
        schema: IssueBeanSchema | Unset
        if isinstance(_schema,  Unset):
            schema = UNSET
        else:
            schema = IssueBeanSchema.from_dict(_schema)




        self_ = d.pop("self", UNSET)

        _transitions = d.pop("transitions", UNSET)
        transitions: list[IssueTransition] | Unset = UNSET
        if _transitions is not UNSET:
            transitions = []
            for transitions_item_data in _transitions:
                transitions_item = IssueTransition.from_dict(transitions_item_data)



                transitions.append(transitions_item)


        _versioned_representations = d.pop("versionedRepresentations", UNSET)
        versioned_representations: IssueBeanVersionedRepresentations | Unset
        if isinstance(_versioned_representations,  Unset):
            versioned_representations = UNSET
        else:
            versioned_representations = IssueBeanVersionedRepresentations.from_dict(_versioned_representations)




        issue_bean = cls(
            changelog=changelog,
            editmeta=editmeta,
            expand=expand,
            fields=fields,
            fields_to_include=fields_to_include,
            id=id,
            key=key,
            names=names,
            operations=operations,
            properties=properties,
            rendered_fields=rendered_fields,
            schema=schema,
            self_=self_,
            transitions=transitions,
            versioned_representations=versioned_representations,
        )

        return issue_bean

