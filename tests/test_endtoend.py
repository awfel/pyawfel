# test end to end workflows.
import csv

from awfel.workflow import load_from_json


class TestBasicWorflow():
    def test_run(self, basic_workflow_path, smtpd):
        """Test the basic workflow run from beginning to end."""
        workflow = load_from_json(basic_workflow_path)
        workflow.start()

        with open('./tests/assets/input.csv') as i, open('./output.csv') as o:
            in_, out = csv.reader(i), csv.reader(o)
            assert len(out) == len(in_)
