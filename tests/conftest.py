import pytest

pytest_plugins = "smtpdfix"


@pytest.fixture
def basic_workflow_path():
    return './tests/assets/basic_workflow.json'
