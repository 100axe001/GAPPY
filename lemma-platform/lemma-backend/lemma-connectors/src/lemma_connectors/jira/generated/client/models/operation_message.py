from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="OperationMessage")



@_attrs_define
class OperationMessage:
    """ 
        Example:
            {'message': 'An example message.', 'statusCode': 200}

        Attributes:
            message (str): The human-readable message that describes the result.
            status_code (int): The status code of the response.
     """

    message: str
    status_code: int





    def to_dict(self) -> dict[str, Any]:
        message = self.message

        status_code = self.status_code


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "message": message,
            "statusCode": status_code,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        status_code = d.pop("statusCode")

        operation_message = cls(
            message=message,
            status_code=status_code,
        )

        return operation_message

