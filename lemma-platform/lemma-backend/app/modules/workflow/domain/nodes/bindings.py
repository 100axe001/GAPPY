"""Typed input bindings for node input mappings."""

from typing import Annotated, Any, Literal, Union

from pydantic import BaseModel, Field


class ExpressionInputBinding(BaseModel):
    """Resolve a value from the run context using a JMESPath expression."""

    type: Literal["expression"] = "expression"
    value: str = Field(
        ...,
        min_length=1,
        description=(
            "JMESPath expression evaluated against the run context. "
            "Example: `start.payload.issue.key` or `collect_input.amount`. "
            "Expressions that resolve to nothing fail the run unless "
            "`optional` is set."
        ),
        examples=["start.payload.issue.key", "collect_input.amount"],
    )
    optional: bool = Field(
        default=False,
        description=(
            "When true, an expression that resolves to nothing yields null "
            "instead of failing the run."
        ),
    )


class LiteralInputBinding(BaseModel):
    """Pass a literal JSON value into the target input without resolution."""

    type: Literal["literal"] = "literal"
    value: Any = Field(
        ...,
        description=(
            "Literal JSON value forwarded exactly as provided. "
            "Use this for strings, numbers, booleans, arrays, or objects that "
            "should not be interpreted as JMESPath expressions."
        ),
        examples=["abc", 42, True, {"channel": "finance"}],
    )


InputBinding = Annotated[
    Union[ExpressionInputBinding, LiteralInputBinding],
    Field(discriminator="type"),
]
