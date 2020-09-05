import secrets

from awfel.activities.base import BaseActivity


class ForEachActivity(BaseActivity):
    def __init__(self,
                 id=None,
                 name=None,
                 description=None,
                 dataset=None,
                 strategy="sequential",
                 workflow=None,
                 steps=None,
                 *args,
                 **kwargs):
        """An activity to handle iterating throught a collection of objects
        and performing a number of steps on each.

        The data passed to each step is always a tuple with id, dict for each
        row and is accessed by calling input['item']. Any changes made to the
        input are written back out once the steps have been completed.

        :param name: The unique name that this item will be recorded as. Note
            that this will appear in any logs, reports, etc. (Required)
        :param description: A readable description of what this step does so
            that anyone in the future will be able to understand the action of
            this step. (Optional)
        :param dataset: Is the reference to the iterable that contains the
            items to be acted on. (Required)
        :param workflow: The workflow container that this activity is part of.
        :param strategy: Whether this should be run sequentially or in parallel
        :type name: string
        :type description: string
        :type dataset: string
        :type workflow: :class:'awfel.Workflow'
        :type strategy: string
        """
        self.id = id or secrets.token_hex(16)
        self.name = name
        self.description = description
        print(workflow.inputs)
        self.dataset = workflow.inputs[dataset]
        self.workflow = workflow
        self.steps = steps
        print(f'in foreach constructor {self.steps}')

        if strategy.lower() not in ['sequential', 'serial', 'parallel']:
            raise ValueError((f"Strategy on {self.name} ForEach must be one "
                              "of 'sequential', 'serial', or 'parallel'."))
        self.strategy = strategy

    def run(self):
        from awfel.actioncontainer import ActionContainer

        dataset = self.dataset.value
        for index, item in enumerate(dataset):
            name = f"{self.name}_{index}"
            kwargs = {'steps': self.steps}
            container = ActionContainer(name=name,
                                        actions=self.workflow.actions,
                                        **kwargs)
            # The way we're handling the inputs isn't great, but we make a copy
            # to avoid mutating the originals.
            container.inputs = self.workflow.inputs.copy()
            container.inputs['item'] = item  # Adds the item to the collection

            if self.strategy == 'parallel':
                # Parallel processing not yet implemented
                raise NotImplementedError()

            container.start()
            # self.dataset[index] = container.inputs['item']
