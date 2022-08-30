#-->Importing Libraries
from time import strftime
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
#-->Setup the engine and initilize the pyttsx3 library
engine=pyttsx3.init('sapi5')
#-->engine is the library
#-->sapi5 is a driver or voice which helps to get the voice 
#for pyttsx3 library for conversion of speech to text
voices=engine.getProperty("voices")
#-->getProperty is a function used to get the voices
engine.setProperty("voice",voices[1].id)
#-->Here 1 is for Female and 0 is for Male
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#-->This function helps computer to speak the written words
#-->runAndWait() function helps speech_recognition library 
# to convert speech to text.When we run this the runAndWait() 
# helps to wait and then recongnize the spoken data and convert 
# it into voice.
def wishme():
    hour=int(datetime.datetime.now().hour) 
    if hour>=0 and hour<=12:
        speak("Hello! Good Morning my Dear Friend!!!")
    elif hour>=12 and hour<18:
        speak("Hello! Good Afternoon my Dear Friend!!!")
    else:
        speak("Hello! Good Evening my Dear Friend!!!")
#-->This function is used with datetime Library!!!!
#-->datetime library is used to give the Date and Time
#-->Here after 12:00   -->It is noon
#but we will consider 1:00 after 12:00 as 13:00 for the correct 
#output because computer does not understand 1:00pm 
#-->Here speak() function is used if we want computer to speak\
    speak("Let me know how can I help You, What are you Looking for?")
#-->This is the Mandatory statement that must be spoken after 
#elif statement!
#-->This wishme() function is over now, here datetime.datetime.now() 
# function help to get the date and accordingly the wishme() 
# function will respond!! 
def takecommand():
    r= sr.Recognizer()
#-->This Statement will help us to recognize and print what ever 
# we are speaking!
    with sr.Microphone() as source:
        print("Listening to you Shreya.....")
        r.pause_threshold=0.5
#-->This statement will help to take a pause for some time and 
# recognize what you have said if it has not understood then it 
# will print not understood.
#Here pause_thershold  Represents the minimum length of silence 
# (in seconds) that will register as the end of a phrase
        audio=r.listen(source)
    try:
        print("Recognizing your Voice........")
        query=r.recognize_google(audio,language="en-in")
#-->As sr function works on APIs, here it will work on Google APIs!!
#Here language can be set up by the user as per his requirement!
        print(f"My Dear Friend You Said: {query}\n")
#-->Here query stores what we have said and \n represents that it 
# will not stop after one instruction it will be a countinuous 
# loop i.e. Infinite Loop.
    except Exception as e:
        print("Shreya say that again Please.....")
        return "None"
    return query
#-->This Function will help to understand whether the computer has 
# understood what we have said,if it has understood what we have 
# spoken it will response accordingly and if not then it will print 
# that i have not understood what you have said!!!
#-->Here the takecommand() funciton ends......
def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
#-->Here 587 is the server!!
    server.ehlo()
#-->Here this statement helps to send the Emails!!
    server.starttls()
#-->This statement helps us to start the smtp Server through which 
# you can send the Emails!!!
    server.login("shreyavbarad72@gmail.com","ekookgwyvlqxhbpo")
#-->Here in this statement we will first give our Email,Password of 
#your Email!!
    server.sendmail("shreyavbarad72@gmail.com",to,content)
    server.close()
#-->This sendEmail() function is used to send Emails!!!
if __name__=="__main__":
#-->The above statement is the main Function of the Python!!
    wishme()
#-->This function is called to Greet ME according to the Time!!
    while True:
        query=takecommand().lower()
#-->This will convert what you have said in Lower Case!!!
        if " wikipedia" in query:
            query=query.replace("on wikipedia","")
            query=query.replace(" wikipedia","")
            query=query.replace(" search ","")
            speak(f"searching{query} on wikipedia")
            result=wikipedia.summary(query,sentences=2)
#-->Here the computer will speak the summary (because of summary()
# function) of the term that you have searched in 2 sentences 
# (because of sentences=2) only the first two sentences.
            speak("here are the results")
            print(result) #Search topic on Wikipedia
#-->By this above statement the result will get Printed!!
            speak(result)
#-->By this above statement the result will be Spoken!!
#-->Here comes the code to open Notepad++
        if "open notepad++" in query:
            npath="C:\\Windows\\Notepad++\\notepad++.exe"
#-->This Statement is for Adding the path of Notepad++ 
#here npath is a variable that stores the path of Notepad++.
            os.startfile(npath)
#-->Here we use the os Library and the file will get opened 
# based on the path given in the Variable npath. 
#-->Here comes the code to Open the Paint
        elif "open paint" in query:
            npath="C:\\Windows\\system32\\mspaint.exe"
#-->This statement is adding the Path of Paint
#Here npath is a variable that stores the path of mspaint
            os.startfile(npath)
#-->Here we use the os Library and the file will get opened based on
#the path given in the Variable npath
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open Great Learning Academy" in query:
            webbrowser.open("https://www.mygreatlearning.com//academy")
#-->Here we have to write the website URL in quotes in Parentheses s
        elif "open google" in query:
            webbrowser.open("google.com")
#-->Here we have to write the google.com in Parenthenses
        elif "tell me the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
#-->Here the strTime is a Variable where the code to get the current 
#Time is written and the format in which u want to Time can be
#written in the Parentheses of strdtime()
            speak(f"My Dear Friend, the Time is {strTime}")
        elif "Email to other Friend" in query:
            try:
                speak("What should I Send?")
                content=takecommand()
#-->Here in the above statement you can speak what u want to send 
# and the computer will convert it into words.
                to="gourivbarad@gmail.com"
#-->Here the above statement will take the Email ID of the receiver
                sendEmail(to,content)
                speak("Shreya, your Email has been Successfully sent!")
            except Exception as e:
                print(e)
#-->This above statement will print the Exception what we are having!! 
                speak("Shreya, I am unable to send the Email..Please address the Error")


        
