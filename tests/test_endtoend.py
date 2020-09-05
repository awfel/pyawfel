# test end to end workflows.
import csv

from awfel.workflow import load_from_json


class TestBasicWorflow():
    def test_run(self, basic_workflow_path, smtpd):
        """Test the basic workflow run from beginning to end."""
        workflow = load_from_json(basic_workflow_path)
        workflow.start()

        with open('./tests/assets/input.csv') as i:
            with open('./tests/assets/output.csv') as o:
                in_, out = csv.reader(i), csv.reader(o)
                in_length = sum([1 for row in in_])
                out_length = sum([1 for row in out])
                assert in_length == out_length

        assert len(smtpd.messages) == 3
