import os

import pytest

pytest_plugins = "smtpdfix"


@pytest.fixture
def basic_workflow_path():
    files = (
        "./tests/assets/basic_workflow.json",
        "./tests/assets/input.csv",
        "./tests/assets/output.csv"
    )
    yield files
    os.remove(files[2])  # Delete output.csv after test has run
