import pytest
from app.modules.connectors.infrastructure.adapters.schema_compiler import (
    PydanticCodeSchemaCompiler,
)


class TestPydanticCodeSchemaCompiler:
    @pytest.fixture
    def compiler(self):
        return PydanticCodeSchemaCompiler()

    def test_to_json_schema_with_target_variable(self, compiler):
        code = """#snippet_type: PYDANTIC_MODEL
#target_variable: MyModel

from pydantic import BaseModel

class MyModel(BaseModel):
    foo: str
"""
        schema = compiler.to_json_schema(code)
        assert schema["title"] == "MyModel"
        assert "foo" in schema["properties"]

    def test_to_json_schema_missing_target_variable_fallback_single_model(
        self, compiler
    ):
        code = """
from pydantic import BaseModel

class UniqueModel(BaseModel):
    bar: int
"""
        schema = compiler.to_json_schema(code)
        assert schema["title"] == "UniqueModel"
        assert "bar" in schema["properties"]

    def test_to_json_schema_missing_target_variable_fallback_input_model(
        self, compiler
    ):
        code = """
from pydantic import BaseModel

class OtherModel(BaseModel):
    x: int

class InputModel(BaseModel):
    y: int
"""
        schema = compiler.to_json_schema(code)
        assert schema["title"] == "InputModel"
        assert "y" in schema["properties"]

    def test_to_json_schema_missing_target_variable_fallback_output_model(
        self, compiler
    ):
        code = """
from pydantic import BaseModel

class OutputModel(BaseModel):
    z: int
"""
        schema = compiler.to_json_schema(code)
        assert schema["title"] == "OutputModel"
        assert "z" in schema["properties"]

    def test_to_json_schema_missing_target_variable_fallback_suffix_model(
        self, compiler
    ):
        code = """
from pydantic import BaseModel

class NestedThing(BaseModel):
    value: int

class ListThingsOutput(BaseModel):
    items: list[NestedThing]
"""
        schema = compiler.to_json_schema(code)
        assert schema["title"] == "ListThingsOutput"
        assert "items" in schema["properties"]

    def test_to_json_schema_empty_code(self, compiler):
        assert compiler.to_json_schema("") == {}
        assert compiler.to_json_schema(None) == {}

    def test_to_json_schema_invalid_code(self, compiler):
        code = "this is not python code"
        # Should return empty dict and log error, not raise
        assert compiler.to_json_schema(code) == {}

    def test_to_json_schema_no_pydantic_models(self, compiler):
        code = """
x = 1
y = 2
"""
        assert compiler.to_json_schema(code) == {}

    def test_to_json_schema_multiple_models_ambiguous(self, compiler):
        code = """
from pydantic import BaseModel

class ModelA(BaseModel):
    a: int

class ModelB(BaseModel):
    b: int
"""
        # Should return empty dict because it can't decide which one to use
        # and there is no InputModel/OutputModel
        assert compiler.to_json_schema(code) == {}

    def test_to_json_schema_with_forward_ref(self, compiler):
        code = """#snippet_type: PYDANTIC_MODEL
#target_variable: ForwardRefModel

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel

class ForwardRefModel(BaseModel):
    child: Optional[ForwardRefModel] = None
"""
        schema = compiler.to_json_schema(code)

        # When recursion is involved, the top-level schema might be a Ref to a definition
        if "$ref" in schema:
            assert "$defs" in schema
            assert "ForwardRefModel" in schema["$defs"]
            model_schema = schema["$defs"]["ForwardRefModel"]
            assert model_schema["title"] == "ForwardRefModel"
            props = model_schema["properties"]["child"]
        else:
            assert schema["title"] == "ForwardRefModel"
            props = schema["properties"]["child"]

        # Handle different Pydantic schema structures for recursive refs
        assert "$ref" in props or ("anyOf" in props and "$ref" in props["anyOf"][0])
