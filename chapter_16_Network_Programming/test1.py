import smtplib


fromAddress = "sender@example.com"
toAddress = "me@my.domain"
msg = "Subject : hello\n\nthis is the body of the message"

server = smtplib.SMTP("localhost", 25)
server.sendmail(fromAddress, toAddress, msg)