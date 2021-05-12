import speech_recognition as sr
import pyttsx3


listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()



def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print("you said:", info)
            talk("you said")
            talk(info)
            return info.lower()
    except:
        print("Sorry could not recognize what you said")  
        talk("could not recognize what you said")
        exit()








#reading mail
import smtplib
import imaplib
import traceback
import time
import email

ORG_EMAIL = "@gmail.com"
FROM_EMAIL = "projectmini25" + ORG_EMAIL
FROM_PWD = "miniproject25"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993
mail = imaplib.IMAP4_SSL(SMTP_SERVER)
mail.login(FROM_EMAIL,FROM_PWD)



def read_email_from_gmail():
    try:
        print("reading latest mail")
        talk("reading latest mail")
        mail.select('inbox')
        data = mail.search(None, 'ALL')
        mail_ids = data[1]
        id_list = mail_ids[0].split()  
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])
        while  latest_email_id >= first_email_id:
            data = mail.fetch(str(latest_email_id), '(RFC822)' )
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr, tuple):
                    msg = email.message_from_string(str(arr[1],'utf-8'))
                    #on subject part
                    email_subject = msg['subject']
                    #on from part
                    email_from = msg['from']
                    print('From: ' +email_from  + '\n')
                    print('Subject : ' +email_subject+ '\n')

                           
            #on body part
            if msg.is_multipart():
            # iterate over email parts
                for part in msg.walk():
                    # extract content type of email
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        # get the email body
                        body = part.get_payload(decode=True).decode()
                    except:
                        pass
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                    # print text/plain emails and skip attachments
                        print(body)
            else:
                # extract content type of email
                content_type = msg.get_content_type()
                # get the email body
                body = msg.get_payload(decode=True).decode()
                if content_type == "text/plain":
                    print(body)

            
            talk(email_from)
            talk(email_subject)
            talk(body)
            print("do you want read next mail:say yes or no")
            talk("do you want read next mail:say yes or no")
           
            text=get_info()         
            if text=="yes":
                latest_email_id-=1
            else :
                print("out of index section")
                talk("out of index section")
                break;
    except Exception as e:
        traceback.print_exc()
