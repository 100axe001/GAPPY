from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.json_node_number_type import JsonNodeNumberType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.json_node_elements import JsonNodeElements
  from ..models.json_node_field_names import JsonNodeFieldNames
  from ..models.json_node_fields import JsonNodeFields





T = TypeVar("T", bound="JsonNode")



@_attrs_define
class JsonNode:
    """ 
        Attributes:
            array (bool | Unset):
            big_decimal (bool | Unset):
            big_integer (bool | Unset):
            big_integer_value (int | Unset):
            binary (bool | Unset):
            binary_value (list[str] | Unset):
            boolean (bool | Unset):
            boolean_value (bool | Unset):
            container_node (bool | Unset):
            decimal_value (float | Unset):
            double (bool | Unset):
            double_value (float | Unset):
            elements (JsonNodeElements | Unset):
            field_names (JsonNodeFieldNames | Unset):
            fields (JsonNodeFields | Unset):
            floating_point_number (bool | Unset):
            int_ (bool | Unset):
            int_value (int | Unset):
            integral_number (bool | Unset):
            long (bool | Unset):
            long_value (int | Unset):
            missing_node (bool | Unset):
            null (bool | Unset):
            number (bool | Unset):
            number_type (JsonNodeNumberType | Unset):
            number_value (float | Unset):
            object_ (bool | Unset):
            pojo (bool | Unset):
            text_value (str | Unset):
            textual (bool | Unset):
            value_as_boolean (bool | Unset):
            value_as_double (float | Unset):
            value_as_int (int | Unset):
            value_as_long (int | Unset):
            value_as_text (str | Unset):
            value_node (bool | Unset):
     """

    array: bool | Unset = UNSET
    big_decimal: bool | Unset = UNSET
    big_integer: bool | Unset = UNSET
    big_integer_value: int | Unset = UNSET
    binary: bool | Unset = UNSET
    binary_value: list[str] | Unset = UNSET
    boolean: bool | Unset = UNSET
    boolean_value: bool | Unset = UNSET
    container_node: bool | Unset = UNSET
    decimal_value: float | Unset = UNSET
    double: bool | Unset = UNSET
    double_value: float | Unset = UNSET
    elements: JsonNodeElements | Unset = UNSET
    field_names: JsonNodeFieldNames | Unset = UNSET
    fields: JsonNodeFields | Unset = UNSET
    floating_point_number: bool | Unset = UNSET
    int_: bool | Unset = UNSET
    int_value: int | Unset = UNSET
    integral_number: bool | Unset = UNSET
    long: bool | Unset = UNSET
    long_value: int | Unset = UNSET
    missing_node: bool | Unset = UNSET
    null: bool | Unset = UNSET
    number: bool | Unset = UNSET
    number_type: JsonNodeNumberType | Unset = UNSET
    number_value: float | Unset = UNSET
    object_: bool | Unset = UNSET
    pojo: bool | Unset = UNSET
    text_value: str | Unset = UNSET
    textual: bool | Unset = UNSET
    value_as_boolean: bool | Unset = UNSET
    value_as_double: float | Unset = UNSET
    value_as_int: int | Unset = UNSET
    value_as_long: int | Unset = UNSET
    value_as_text: str | Unset = UNSET
    value_node: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.json_node_elements import JsonNodeElements
        from ..models.json_node_field_names import JsonNodeFieldNames
        from ..models.json_node_fields import JsonNodeFields
        array = self.array

        big_decimal = self.big_decimal

        big_integer = self.big_integer

        big_integer_value = self.big_integer_value

        binary = self.binary

        binary_value: list[str] | Unset = UNSET
        if not isinstance(self.binary_value, Unset):
            binary_value = self.binary_value



        boolean = self.boolean

        boolean_value = self.boolean_value

        container_node = self.container_node

        decimal_value = self.decimal_value

        double = self.double

        double_value = self.double_value

        elements: dict[str, Any] | Unset = UNSET
        if not isinstance(self.elements, Unset):
            elements = self.elements.to_dict()

        field_names: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_names, Unset):
            field_names = self.field_names.to_dict()

        fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()

        floating_point_number = self.floating_point_number

        int_ = self.int_

        int_value = self.int_value

        integral_number = self.integral_number

        long = self.long

        long_value = self.long_value

        missing_node = self.missing_node

        null = self.null

        number = self.number

        number_type: str | Unset = UNSET
        if not isinstance(self.number_type, Unset):
            number_type = self.number_type.value


        number_value = self.number_value

        object_ = self.object_

        pojo = self.pojo

        text_value = self.text_value

        textual = self.textual

        value_as_boolean = self.value_as_boolean

        value_as_double = self.value_as_double

        value_as_int = self.value_as_int

        value_as_long = self.value_as_long

        value_as_text = self.value_as_text

        value_node = self.value_node


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if array is not UNSET:
            field_dict["array"] = array
        if big_decimal is not UNSET:
            field_dict["bigDecimal"] = big_decimal
        if big_integer is not UNSET:
            field_dict["bigInteger"] = big_integer
        if big_integer_value is not UNSET:
            field_dict["bigIntegerValue"] = big_integer_value
        if binary is not UNSET:
            field_dict["binary"] = binary
        if binary_value is not UNSET:
            field_dict["binaryValue"] = binary_value
        if boolean is not UNSET:
            field_dict["boolean"] = boolean
        if boolean_value is not UNSET:
            field_dict["booleanValue"] = boolean_value
        if container_node is not UNSET:
            field_dict["containerNode"] = container_node
        if decimal_value is not UNSET:
            field_dict["decimalValue"] = decimal_value
        if double is not UNSET:
            field_dict["double"] = double
        if double_value is not UNSET:
            field_dict["doubleValue"] = double_value
        if elements is not UNSET:
            field_dict["elements"] = elements
        if field_names is not UNSET:
            field_dict["fieldNames"] = field_names
        if fields is not UNSET:
            field_dict["fields"] = fields
        if floating_point_number is not UNSET:
            field_dict["floatingPointNumber"] = floating_point_number
        if int_ is not UNSET:
            field_dict["int"] = int_
        if int_value is not UNSET:
            field_dict["intValue"] = int_value
        if integral_number is not UNSET:
            field_dict["integralNumber"] = integral_number
        if long is not UNSET:
            field_dict["long"] = long
        if long_value is not UNSET:
            field_dict["longValue"] = long_value
        if missing_node is not UNSET:
            field_dict["missingNode"] = missing_node
        if null is not UNSET:
            field_dict["null"] = null
        if number is not UNSET:
            field_dict["number"] = number
        if number_type is not UNSET:
            field_dict["numberType"] = number_type
        if number_value is not UNSET:
            field_dict["numberValue"] = number_value
        if object_ is not UNSET:
            field_dict["object"] = object_
        if pojo is not UNSET:
            field_dict["pojo"] = pojo
        if text_value is not UNSET:
            field_dict["textValue"] = text_value
        if textual is not UNSET:
            field_dict["textual"] = textual
        if value_as_boolean is not UNSET:
            field_dict["valueAsBoolean"] = value_as_boolean
        if value_as_double is not UNSET:
            field_dict["valueAsDouble"] = value_as_double
        if value_as_int is not UNSET:
            field_dict["valueAsInt"] = value_as_int
        if value_as_long is not UNSET:
            field_dict["valueAsLong"] = value_as_long
        if value_as_text is not UNSET:
            field_dict["valueAsText"] = value_as_text
        if value_node is not UNSET:
            field_dict["valueNode"] = value_node

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.json_node_elements import JsonNodeElements
        from ..models.json_node_field_names import JsonNodeFieldNames
        from ..models.json_node_fields import JsonNodeFields
        d = dict(src_dict)
        array = d.pop("array", UNSET)

        big_decimal = d.pop("bigDecimal", UNSET)

        big_integer = d.pop("bigInteger", UNSET)

        big_integer_value = d.pop("bigIntegerValue", UNSET)

        binary = d.pop("binary", UNSET)

        binary_value = cast(list[str], d.pop("binaryValue", UNSET))


        boolean = d.pop("boolean", UNSET)

        boolean_value = d.pop("booleanValue", UNSET)

        container_node = d.pop("containerNode", UNSET)

        decimal_value = d.pop("decimalValue", UNSET)

        double = d.pop("double", UNSET)

        double_value = d.pop("doubleValue", UNSET)

        _elements = d.pop("elements", UNSET)
        elements: JsonNodeElements | Unset
        if isinstance(_elements,  Unset):
            elements = UNSET
        else:
            elements = JsonNodeElements.from_dict(_elements)




        _field_names = d.pop("fieldNames", UNSET)
        field_names: JsonNodeFieldNames | Unset
        if isinstance(_field_names,  Unset):
            field_names = UNSET
        else:
            field_names = JsonNodeFieldNames.from_dict(_field_names)




        _fields = d.pop("fields", UNSET)
        fields: JsonNodeFields | Unset
        if isinstance(_fields,  Unset):
            fields = UNSET
        else:
            fields = JsonNodeFields.from_dict(_fields)




        floating_point_number = d.pop("floatingPointNumber", UNSET)

        int_ = d.pop("int", UNSET)

        int_value = d.pop("intValue", UNSET)

        integral_number = d.pop("integralNumber", UNSET)

        long = d.pop("long", UNSET)

        long_value = d.pop("longValue", UNSET)

        missing_node = d.pop("missingNode", UNSET)

        null = d.pop("null", UNSET)

        number = d.pop("number", UNSET)

        _number_type = d.pop("numberType", UNSET)
        number_type: JsonNodeNumberType | Unset
        if isinstance(_number_type,  Unset):
            number_type = UNSET
        else:
            number_type = JsonNodeNumberType(_number_type)




        number_value = d.pop("numberValue", UNSET)

        object_ = d.pop("object", UNSET)

        pojo = d.pop("pojo", UNSET)

        text_value = d.pop("textValue", UNSET)

        textual = d.pop("textual", UNSET)

        value_as_boolean = d.pop("valueAsBoolean", UNSET)

        value_as_double = d.pop("valueAsDouble", UNSET)

        value_as_int = d.pop("valueAsInt", UNSET)

        value_as_long = d.pop("valueAsLong", UNSET)

        value_as_text = d.pop("valueAsText", UNSET)

        value_node = d.pop("valueNode", UNSET)

        json_node = cls(
            array=array,
            big_decimal=big_decimal,
            big_integer=big_integer,
            big_integer_value=big_integer_value,
            binary=binary,
            binary_value=binary_value,
            boolean=boolean,
            boolean_value=boolean_value,
            container_node=container_node,
            decimal_value=decimal_value,
            double=double,
            double_value=double_value,
            elements=elements,
            field_names=field_names,
            fields=fields,
            floating_point_number=floating_point_number,
            int_=int_,
            int_value=int_value,
            integral_number=integral_number,
            long=long,
            long_value=long_value,
            missing_node=missing_node,
            null=null,
            number=number,
            number_type=number_type,
            number_value=number_value,
            object_=object_,
            pojo=pojo,
            text_value=text_value,
            textual=textual,
            value_as_boolean=value_as_boolean,
            value_as_double=value_as_double,
            value_as_int=value_as_int,
            value_as_long=value_as_long,
            value_as_text=value_as_text,
            value_node=value_node,
        )

        return json_node

