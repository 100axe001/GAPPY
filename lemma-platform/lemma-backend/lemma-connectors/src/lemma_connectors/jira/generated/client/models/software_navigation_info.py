from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SoftwareNavigationInfo")



@_attrs_define
class SoftwareNavigationInfo:
    """ 
        Attributes:
            board_id (int | Unset):
            board_name (str | Unset):
            simple_board (bool | Unset):
            total_boards_in_project (int | Unset):
     """

    board_id: int | Unset = UNSET
    board_name: str | Unset = UNSET
    simple_board: bool | Unset = UNSET
    total_boards_in_project: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        board_id = self.board_id

        board_name = self.board_name

        simple_board = self.simple_board

        total_boards_in_project = self.total_boards_in_project


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if board_id is not UNSET:
            field_dict["boardId"] = board_id
        if board_name is not UNSET:
            field_dict["boardName"] = board_name
        if simple_board is not UNSET:
            field_dict["simpleBoard"] = simple_board
        if total_boards_in_project is not UNSET:
            field_dict["totalBoardsInProject"] = total_boards_in_project

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        board_id = d.pop("boardId", UNSET)

        board_name = d.pop("boardName", UNSET)

        simple_board = d.pop("simpleBoard", UNSET)

        total_boards_in_project = d.pop("totalBoardsInProject", UNSET)

        software_navigation_info = cls(
            board_id=board_id,
            board_name=board_name,
            simple_board=simple_board,
            total_boards_in_project=total_boards_in_project,
        )


        software_navigation_info.additional_properties = d
        return software_navigation_info

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
