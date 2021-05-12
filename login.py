import smtplib
import time
import imaplib
import email
import traceback


ORG_EMAIL = "email name.com"
FROM_EMAIL = "username" + ORG_EMAIL
FROM_PWD = "password"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993
mail = imaplib.IMAP4_SSL(SMTP_SERVER)
mail.login(FROM_EMAIL,FROM_PWD)
