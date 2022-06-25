# test end to end workflows.
import csv

from awfel.workflow import load_from_json


class TestBasicWorkflow():
    def test_run(self, basic_workflow_path, mocker):
        """Test the basic workflow run from beginning to end."""
        mocker.patch(
            "awfel.activities.sendemail.SendEmailActivity.send_message",
            return_value=None
        )

        definition, input, output = basic_workflow_path
        workflow = load_from_json(definition)
        workflow.start()

        with open(input) as i, open(output) as o:
            in_, out = csv.reader(i), csv.reader(o)
            in_length = sum([1 for row in in_])
            out_length = sum([1 for row in out])
            assert in_length == out_length

        assert len(smtpd.messages) == 3
