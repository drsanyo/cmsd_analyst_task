import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from repositories.configurationRepository import configurationRepository


class emailSender:
    def sendAutomaticEmailEmail(self, html):

        emailSendingOptions = configurationRepository().getEmailSendingOptions()
        sender = emailSendingOptions.sender
        receiver = emailSendingOptions.receiver

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = emailSendingOptions.subject
        msg['From'] = sender
        msg['To'] = receiver

        part2 = MIMEText(html, 'html')
        msg.attach(part2)

        with smtplib.SMTP(emailSendingOptions.address, emailSendingOptions.port) as server:
            server.login(emailSendingOptions.user, emailSendingOptions.password)
            server.sendmail(sender, receiver, msg.as_string())