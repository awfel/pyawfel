import pytest
from awfel.errors.workflowerror import WorkflowError
from awfel.inputs.base import BaseInput


def test_init():
    base = BaseInput("Test", "Test input")
    assert base.name == "Test"
    assert base.description == "Test input"


def test_init_error():
    with pytest.raises(WorkflowError) as error:
        base = BaseInput()
        assert base.name is None
        assert error.type is WorkflowError
