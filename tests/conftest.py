import pytest

from smtpdfix import smtpd  # noqa: F401 (unused import)


@pytest.fixture
def basic_workflow_path():
    return './tests/assets/basic_workflow.json'
