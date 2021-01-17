from awfel.activities import BaseActivity


class IfActivity(BaseActivity):
    def __init__(self,
                 name,
                 description=None,
                 conditions=[],
                 steps=[],
                 workflow=None):
        """If all of the conditions are met then perform the steps.

        :param name: a name, unique to the container, for the activity.
        :param description: the description of the activity.
        """
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
