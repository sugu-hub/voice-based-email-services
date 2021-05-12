import smtplib
import time
import imaplib
import email
import traceback


ORG_EMAIL = "@gmail.com"
FROM_EMAIL = "projectmini25" + ORG_EMAIL
FROM_PWD = "miniproject25"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993
mail = imaplib.IMAP4_SSL(SMTP_SERVER)
mail.login(FROM_EMAIL,FROM_PWD)