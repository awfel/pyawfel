Activities
==========

Introduction
------------

Activities are the building blocks from which Awfel workflows are built.

They exist in two different varieties. The first could be termed atomic 
activities and are to do things. The others are control structures which allow
you to tell Awfel how to process your data.

Already Defined Activities
--------------------------

Control Structures
~~~~~~~~~~~~~~~~~~

Control structures allow you to define the flow of data and order of
activities in your workflows.

.. method:: ForEachActivity(self, name, description, item_name="item",
                **kwargs)

    For each item in the specified iterable perform the actions. The item is
    always provided as item unless the item_name is specified in the
    arguments.

.. method:: IfActivity(self, name, description, conditions, **kwargs)

    Control structure that allows you to test for one or more conditions and
    then performs the action.


Creating your own
-----------------
Creating your own activities and incorporating them into Awfel is easy using
the provided base classes.

for example:

.. code-block:: python

    from awfel.activities import BaseActivity

    class SendReminderEmailActivity(BaseActivity):
        def __init__(self, name, description, to, from_):
            """Sends a subsequent email based on some conditions."""
            self.name = name
            self.description = description
            self._to = to
            self._from = from_

        def build_msg(self):
            from email import Message

            msg = Message()
            msg['to'] = self._address
            msg['from'] = self._from

        def run(self):
            from os import getenv
            from smtplib import SMTP

            host = getenv("SMTP_HOSTNAME", "127.0.0.1")
            port = getenv("SMTP_PORT", 25)
            with SMTP(host, port) as mail:
                mail.sendmessage(build_msg())
