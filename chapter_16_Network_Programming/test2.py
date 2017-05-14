import smtplib

fromAddress = "sender@example.com"
toAddress = "to@example.com"
msg = "test message"

server = smtplib.SMTP("localhost", 25)
server.sendmail(fromAddress, toAddress, msg)
