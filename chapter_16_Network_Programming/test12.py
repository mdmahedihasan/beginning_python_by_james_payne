import imaplib
import email


imap = imaplib.IMAP4("imap.example.com")
imap.login("[username]", "[password]")