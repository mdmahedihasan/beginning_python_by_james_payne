import os
import sys
import smtplib
import mimetypes

from optparse import OptionParser
from email import encoders
from email.message import Message

message = Message()
message["Subject"] = "hello"
message.set_payload("this is the body of the message")
print(str(message))