from awfel.activities import BaseActivity


class IfActivity(BaseActivity):
    def __init__(self,
                 name,
                 description=None,
                 conditions=[],
                 steps=[],
                 workflow=None):
        """If all of the conditions are met then perform the steps."""
        self.name = name
        self.description = description

        # Process the conditions
        for c in conditions:
            # do something here.
            continue

    def run(self):
        # if not everything passes then raise a workflow.stop
        self.workflow.stop()

        raise NotImplementedError()
