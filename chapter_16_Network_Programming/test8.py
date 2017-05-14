import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

msg = MIMEMultipart()
filename = ("/home/mahedi/ok.jpg")

msg["To"] = "to@example.com"
msg["From"] = "me@example.com"
msg["Subject"] = "some picture"

# pic = open("/home/mahedi/ok.jpg", 'rb')
pic = open(filename, 'rb')
img = MIMEImage(pic.read())
pic.close()

print(str(msg))
msg.attach(img)

# sendit = smtplib.SMTP()
# sendit.connect()
# sendit.sendmail("", "", msg.as_string())
# sendit.close()