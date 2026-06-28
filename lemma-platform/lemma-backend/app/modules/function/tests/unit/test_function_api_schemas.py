import pytest
from pydantic import ValidationError

from app.modules.function.api.schemas.function_schemas import CreateFunctionRequest


@pytest.mark.parametrize(
    "field_name",
    ["input_schema", "output_schema", "config_schema", "allowed_actions"],
)
def test_create_function_request_rejects_response_only_fields(field_name):
    with pytest.raises(ValidationError):
        CreateFunctionRequest.model_validate(
            {
                "name": "adder",
                "code": "def adder(input):\n    return input\n",
                field_name: {},
            }
        )
