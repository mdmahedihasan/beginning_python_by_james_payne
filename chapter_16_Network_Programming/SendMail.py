import mimetypes

from email import encoders as Encoders
from email.message import Message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.nonmultipart import MIMENonMultipart
from smtplib import SMTP


class StartMessage:
    def __init__(self, fromAdd, toAdd, subject, body):
        self.msg = Message()
        self.msg.set_payload(body)
        self["Subject"] = subject
        self.setFrom(fromAdd)
        self.setTo(toAdd)
        self.hasAttachments = False

    def setFrom(self, fromAdd):
        if not fromAdd or not type(fromAdd) == type(""):
            raise Exception("a message must have one and only one sender")
        self["From"] = fromAdd

    def setTo(self, to):
        if not to:
            raise Exception("a message must have at least one recipient")
        self._addresses(to, "To")
        self.to = to

    def setCc(self, cc):
        self._addresses(cc, "Cc")

    def addAttachment(self, attachment, filename, mimetype=None):
        if not mimetype:
            mimetype = mimetypes.guess_type(filename)[0]
        if not mimetype:
            raise Exception("could not determine MIME type for ", filename)
        if "/" in mimetype:
            major, minor = mimetype.split("/")
        else:
            major = mimetype
            minor = None
        if not self.hasAttachments:
            body = self.msg.set_payload()
            newMsg = MIMEMultipart()
            newMsg.attach(MIMEText(body))

            for header, value in self.msg.items():
                newMsg[header] = value

            self.msg = newMsg
            self.hasAttachments = True
        subMessage = MIMENonMultipart(major, minor, name=filename)
        subMessage.set_payload(attachment)

        if major == "text":
            encoder = Encoders.encode_quopri
        else:
            encoder = Encoders.encode_base64
        encoder(subMessage)
        self.msg.attach(subMessage)

    def _addresses(self, addresses, key):
        if hasattr(addresses, "__iter__"):
            addresses = ''.join(addresses)
        self[key] = addresses

    def __getitem__(self, key):
        return self.msg[key]

    def __setitem__(self, key, value):
        self.msg[key] = value

    def __getattr__(self, key):
        return getattr(self.msg, key)

    def __str__(self):
        return self.msg.as_string()



class MailServer(SMTP):
    def __init__(self, server, serverUser=None, serverPassword=None, port=25):
        SMTP.__init__(self, server, port)
        self.user = serverUser
        self.password = serverPassword
        # self.set_debuglevel(True)

    def sendMessage(self, message):
        if self.user:
            self.login(self.user, self.password)

        destinations = message.to
        if hasattr(destinations, "__iter__"):
            destinations = map(self._cleanAddress, destinations)
        else:
            destinations = self._cleanAddress(destinations)
        self.sendmail(message["From"], destinations, str(message))

    def _cleanAddress(self, address):
        parts = address.split("<", 1)
        if len(parts) > 1:
            newAddress = parts[1]
            endAddress = newAddress.find(">")
            if endAddress != -1:
                address = newAddress[:endAddress]
        return address


msg = StartMessage("Me <me@example.com>", "You <you@example.com>", "your picture", "pic of you")
# print(msg)

msg.addAttachment(open("/home/mahedi/ok.jpg").read(), 'ok.jpg')
# print(str(msg))