from awfel.activities.base import BaseActivity


class SendEmailActivity(BaseActivity):
    def __init__(self,
                 name=None,
                 description=None,
                 to="",
                 reply_to="",
                 subject="",
                 body="",
                 strategy="sequential",
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
        if isinstance(to, dict):
            # Handle spawning the child instances for each adddress to send the
            # emails.
            raise NotImplementedError()

        raise NotImplementedError()
