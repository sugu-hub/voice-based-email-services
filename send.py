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





#sending mail
import smtplib
from email.message import EmailMessage
def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('projectmini25@gmail.com', 'miniproject25')
    email = EmailMessage()
    email['From'] = 'projectmini25@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'pqr': 'projectmini25@gmail.com',
    'bts': 'ammulu24682@gmail.com',
    'abc': 'sarithachinnari981@gmail.com',
    'lisa': 'divya060814@gmail.com',
    'xyz': 'sugureshwar.d@gmail.com'
}


def get_email_info():
    print('To Whom you want to send email')
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk(receiver)
    talk('What is the subject of your email?')
    print('What is the subject of your email?')
    subject = get_info()
    print('Tell me the text in your email')
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    print('Hey  Your email is sent')
    talk('Hey  Your email is sent')
    print('Do you want to send more email?')
    talk('Do you want to send more email?')
    talk("say yes or no")
    send_more = get_info()
    if 'yes' in send_more:
     get_email_info()
    else:
     print('out from send mail section')
     talk('out from send mail section')