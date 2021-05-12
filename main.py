import speech_recognition as sr
import pyttsx3
import send as se
import read as r




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



print("project:voice based email services for blind")
talk("project:voice based email services for blind")

print("do you want to login into your gmail : say yes or no")
talk("do you want to login into your gmail : say yes or no")
text=get_info()




if text=="yes":
	print("your login under process")
	talk("your login under process")
	import login
	print("your login succesful")
	talk("your login succesful")
	#-----------------------------------------------------------------------------
    


	while True:
		print("1 : compose a mail")
		talk("1 : compose a mail")
		print("2 : check your inbox")
		talk("2 : check your inbox")
		print("3 : logout")
		talk("3 : logout")
		print("give your option 1 or 2 or 3")
		talk("give your option 1 or 2 or 3")
		text=get_info()
        

		if text=="1":
			se.get_email_info()

		elif text=="2" or text=="tu":
			r.read_email_from_gmail()
			
		elif text=="3" or text=="tree":

			print("you succesfully logout")
			talk("you succesfully logout")
			exit()
		else:
			print("not a valid option")
			talk("not a valid option")
			exit()
else:
	print("okay see you again bye bye")
	talk("okay see you again bye bye")