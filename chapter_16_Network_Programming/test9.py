import smtplib

fromAddress = "sender@example.com"
toAddress = "to@example.com"
msg = "this is test"

server = smtplib.SMTP("localhost", 25)
server.sendmail(fromAddress, toAddress, msg)