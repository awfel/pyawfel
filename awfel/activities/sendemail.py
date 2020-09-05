import logging
from smtplib import SMTP
from email.message import EmailMessage
import secrets

from awfel.activities.base import BaseActivity

log = logging.getLogger(__name__)
fields = ['to', 'reply_to', 'subject', 'body']


class SendEmailActivity(BaseActivity):
    def __init__(self,
                 id=None,
                 name=None,
                 description=None,
                 smtphost='localhost',
                 smtpport=8025,
                 strategy='sequential',
                 dataset='item',
                 template=None,
                 workflow=None,
                 *args,
                 **kwargs):
        """An activity to send an email based on some set of inputs.

        :param name: The unique name of the activity.
        :param description: The readable description that describes what the
                            activity is.
        :param to: The address that the email will be sent to.
        :param reply_to: The address that will be included as the reply_to for
                         the email message.
        :param subject: The subject for the email message.
        :param body: The body of the email.
        :param strategy: Whether to process the emails sequentially or in
                         parallel. Default is sequentially.
        :type name: string
        :type description: string
        :type to: string, dict (for a column reference)
        :type reply_to: string, dict (for a column reference)
        :type subject: string, dict (for a column reference or template)
        :type body: string, dict (for a column reference or template)

        .. note:: If the 'to' is a dictionary specifying a field to use this
                  will spawn child activities to send each email individually.
        """
        # Removed
        #  smtphost='localhost',
        #  smtpport=8025,
        #  to='',
        #  reply_to='',
        #  subject='',
        #  body='',
        self.id = id or secrets.token_hex(8)
        self.name = name
        self.description = description
        self.smtphost = smtphost
        self.smtpport = smtpport
        self.workflow = workflow
        self.template = template
        self.dataset = self.workflow.inputs[dataset]
        if not isinstance(self.dataset, dict):
            self.dataset = self.dataset.value

        self.config = dict()
        for key in fields:
            self.config[key] = kwargs.get(key, '')

    def function(self, value, item):
        if isinstance(value, dict):
            if value['field']:
                # return the field
                return item.get(value['field'], '')
            if value['expr']:
                def today(self):
                    from datetime import datetime
                    return datetime.today()

                return eval(value['expr'])

        return value

    def send_message(self, host, port, msg):
        with SMTP(host, port) as smtp_client:
            smtp_client.send_message(msg)

    def run(self):
        """Send the email."""
        _config = dict()
        for key, value in self.config.items():
            _config[key] = self.function(value, self.dataset)

        host = self.smtphost
        port = self.smtpport
        msg_template = self.workflow.inputs[self.template].value()
        msg = EmailMessage()
        msg["Subject"] = "Foo"
        msg["Sender"] = "from.addr@example.org"
        msg["To"] = "to.addr@example.org"
        msg.set_content(msg_template.render(item=self.dataset))

        self.send_message(host, port, msg)
