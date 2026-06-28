"""ExpressionEngine: the single JMESPath expression system."""

import pytest

from app.modules.workflow.domain.errors import (
    ContextPathError,
    ExpressionSyntaxError,
)
from app.modules.workflow.domain.expressions import ExpressionEngine


DATA = {
    "approval": {"approved": True, "amount": 120, "tags": ["a"]},
    "intake": {"merchant": "Uber", "empty": "", "items": []},
}


def test_compile_rejects_invalid_expressions():
    with pytest.raises(ExpressionSyntaxError):
        ExpressionEngine.compile("][")
    with pytest.raises(ExpressionSyntaxError):
        ExpressionEngine.compile("")
    ExpressionEngine.compile("approval.approved == `true`")


def test_evaluate_returns_none_for_missing_paths():
    assert ExpressionEngine.evaluate("intake.missing.deep", DATA) is None


def test_evaluate_required_raises_on_none():
    with pytest.raises(ContextPathError):
        ExpressionEngine.evaluate_required("intake.missing", DATA)
    assert ExpressionEngine.evaluate_required("intake.merchant", DATA) == "Uber"


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("approval.approved == `true`", True),
        ("approval.approved == `false`", False),
        ("approval.amount > `100`", True),
        ("approval.amount > `100` && intake.merchant == 'Uber'", True),
        ("approval.amount < `100` || intake.merchant == 'Uber'", True),
        ("!(approval.approved)", False),
        ("contains(intake.merchant, 'Ub')", True),
        ("length(approval.tags) > `0`", True),
        # truthiness table
        ("intake.missing", False),  # None
        ("intake.empty", False),  # ""
        ("intake.items", False),  # []
        ("approval", True),  # non-empty dict
        ("`true`", True),
        ("`0`", True),  # JMESPath convention: 0 is truthy
    ],
)
def test_condition_truthiness(expression, expected):
    assert ExpressionEngine.evaluate_condition(expression, DATA) is expected
