import os
import sys

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

filename = "/home/mahedi/ok.jpg"
msg = MIMEMultipart()

msg["From"] = "from@example.com"
msg["To"] = "to@example.com"
msg["Subject"] = "this is test"

text = MIMEText("here is the picture")
msg.attach(text)

image = MIMEImage(open(filename, 'rb').read(), name=os.path.split(filename)[1])
msg.attach(image)

# print(str(msg))
print(msg)