from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.id_or_key_bean import IdOrKeyBean
  from ..models.issue_context_variable import IssueContextVariable
  from ..models.jexp_issues import JexpIssues
  from ..models.json_context_variable import JsonContextVariable
  from ..models.user_context_variable import UserContextVariable





T = TypeVar("T", bound="JiraExpressionEvalContextBean")



@_attrs_define
class JiraExpressionEvalContextBean:
    """ 
        Attributes:
            board (int | Unset): The ID of the board that is available under the `board` variable when evaluating the
                expression.
            custom (list[IssueContextVariable | JsonContextVariable | UserContextVariable] | Unset): Custom context
                variables and their types. These variable types are available for use in a custom context:

                 *  `user`: A [user](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-reference#user)
                specified as an Atlassian account ID.
                 *  `issue`: An [issue](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
                reference#issue) specified by ID or key. All the fields of the issue object are available in the Jira
                expression.
                 *  `json`: A JSON object containing custom content.
                 *  `list`: A JSON list of `user`, `issue`, or `json` variable types.
            customer_request (int | Unset): The ID of the customer request that is available under the `customerRequest`
                variable when evaluating the expression. This is the same as the ID of the underlying Jira issue, but the
                customer request context variable will have a different type.
            issue (IdOrKeyBean | Unset):
            issues (JexpIssues | Unset): The JQL specifying the issues available in the evaluated Jira expression under the
                `issues` context variable.
            project (IdOrKeyBean | Unset):
            service_desk (int | Unset): The ID of the service desk that is available under the `serviceDesk` variable when
                evaluating the expression.
            sprint (int | Unset): The ID of the sprint that is available under the `sprint` variable when evaluating the
                expression.
     """

    board: int | Unset = UNSET
    custom: list[IssueContextVariable | JsonContextVariable | UserContextVariable] | Unset = UNSET
    customer_request: int | Unset = UNSET
    issue: IdOrKeyBean | Unset = UNSET
    issues: JexpIssues | Unset = UNSET
    project: IdOrKeyBean | Unset = UNSET
    service_desk: int | Unset = UNSET
    sprint: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.id_or_key_bean import IdOrKeyBean
        from ..models.issue_context_variable import IssueContextVariable
        from ..models.jexp_issues import JexpIssues
        from ..models.json_context_variable import JsonContextVariable
        from ..models.user_context_variable import UserContextVariable
        board = self.board

        custom: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom, Unset):
            custom = []
            for custom_item_data in self.custom:
                custom_item: dict[str, Any]
                if isinstance(custom_item_data, UserContextVariable):
                    custom_item = custom_item_data.to_dict()
                elif isinstance(custom_item_data, IssueContextVariable):
                    custom_item = custom_item_data.to_dict()
                else:
                    custom_item = custom_item_data.to_dict()

                custom.append(custom_item)



        customer_request = self.customer_request

        issue: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issue, Unset):
            issue = self.issue.to_dict()

        issues: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issues, Unset):
            issues = self.issues.to_dict()

        project: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        service_desk = self.service_desk

        sprint = self.sprint


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if board is not UNSET:
            field_dict["board"] = board
        if custom is not UNSET:
            field_dict["custom"] = custom
        if customer_request is not UNSET:
            field_dict["customerRequest"] = customer_request
        if issue is not UNSET:
            field_dict["issue"] = issue
        if issues is not UNSET:
            field_dict["issues"] = issues
        if project is not UNSET:
            field_dict["project"] = project
        if service_desk is not UNSET:
            field_dict["serviceDesk"] = service_desk
        if sprint is not UNSET:
            field_dict["sprint"] = sprint

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.id_or_key_bean import IdOrKeyBean
        from ..models.issue_context_variable import IssueContextVariable
        from ..models.jexp_issues import JexpIssues
        from ..models.json_context_variable import JsonContextVariable
        from ..models.user_context_variable import UserContextVariable
        d = dict(src_dict)
        board = d.pop("board", UNSET)

        _custom = d.pop("custom", UNSET)
        custom: list[IssueContextVariable | JsonContextVariable | UserContextVariable] | Unset = UNSET
        if _custom is not UNSET:
            custom = []
            for custom_item_data in _custom:
                def _parse_custom_item(data: object) -> IssueContextVariable | JsonContextVariable | UserContextVariable:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_context_variable_type_0 = UserContextVariable.from_dict(data)



                        return componentsschemas_custom_context_variable_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_custom_context_variable_type_1 = IssueContextVariable.from_dict(data)



                        return componentsschemas_custom_context_variable_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_custom_context_variable_type_2 = JsonContextVariable.from_dict(data)



                    return componentsschemas_custom_context_variable_type_2

                custom_item = _parse_custom_item(custom_item_data)

                custom.append(custom_item)


        customer_request = d.pop("customerRequest", UNSET)

        _issue = d.pop("issue", UNSET)
        issue: IdOrKeyBean | Unset
        if isinstance(_issue,  Unset):
            issue = UNSET
        else:
            issue = IdOrKeyBean.from_dict(_issue)




        _issues = d.pop("issues", UNSET)
        issues: JexpIssues | Unset
        if isinstance(_issues,  Unset):
            issues = UNSET
        else:
            issues = JexpIssues.from_dict(_issues)




        _project = d.pop("project", UNSET)
        project: IdOrKeyBean | Unset
        if isinstance(_project,  Unset):
            project = UNSET
        else:
            project = IdOrKeyBean.from_dict(_project)




        service_desk = d.pop("serviceDesk", UNSET)

        sprint = d.pop("sprint", UNSET)

        jira_expression_eval_context_bean = cls(
            board=board,
            custom=custom,
            customer_request=customer_request,
            issue=issue,
            issues=issues,
            project=project,
            service_desk=service_desk,
            sprint=sprint,
        )

        return jira_expression_eval_context_bean

