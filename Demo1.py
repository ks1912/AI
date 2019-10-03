#AI


import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wi
import webbrowser as wb
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio): # Will speak the argument's that will be given to it
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    time = int(datetime.datetime.now().hour)
    if time >= 0 and time<12:
        speak("Good Morning Kunal")

    elif time >= 12 and time <18:
        speak("Good Afternoon Kunal")

    else:
        speak("Good Evening Kunal")

    speak("I am your AI Sir , How may I help you ?")


def takeCommand():
        # It take input in microphone format and change that in string format

        r1 = sr.Recognizer()
        with sr.Microphone() as source:
            print("I AM LISTINING SIR IF U WAIT FOR 2 Seconds I will stop my LISTINING ...")
            r1.pause_threshold = 2
            audio = r1.listen(source)

        try:
            print("RECOGNIZING ...")
            query = r1.recognize_google(audio, language='en-in')
            print(f"USER SAID :{query}\n")
            # speak(query) It is used to speak what user said

        except Exception as e:
            print(e)
            print("NOT ABLE To UNDERSTAND ... SAY AGAIN ...")
            return "None"
        return query

if __name__=="__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

        # LOGIC FOR EXECUTING TASK BASED ON QUERY

        if 'wikipedia' in query: # Search for wikipedia in input voice if available execute this if statement
            speak('Searching Wikipedia')  # It will speak WIKIPEDIA
            query = query.replace("Wikipedia", "") # WIKIPEDIA will be replaced by blank  and then execute
            results = wi.summary(query, sentences=3) # READ 3 Sentences from Wikipedia
            speak("According to Wikipedia") # AI will speak ACCORDING TO WIKIPEDIA AND THEN IT WILL START SAYING
            print(results) # print the results like 3 lines of wikipidea
            speak(results) # speak the results like 3 lines of wikipedia

        elif 'youtube' in query:
            speak("Okay Sir")
            wb.open("youtube.com")

        elif 'google' in query:
            speak("Okay Sir")
            wb.open("google.com")

        elif 'stack' in query:
            speak("Okay Sir")
            wb.open("stackoverflow.com")

        elif 'facebook' in query:
            speak("Okay Sir")
            wb.open("facebook.com")

        elif 'movie' in query:
            movie_dir = "F:\\"
            movie= os.listdir(movie_dir)
            print(movie)
            speak("Sir, please ENTER MOVIE NO BELLOW U WANT TO PRINT COUNTING START FROM 0, 1, 2, 3...  \n  ")
            os.startfile(os.path.join(movie_dir, movie[int(input("ENTER HERE -> "))])) # we can use random module so that pc will play any random movie ... we can directly assign a specific movie no by giving it's location or else we can take input from user to play a movie of there choice

        elif 'time' in query:
            speak("Okay Sir")
            taketime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {taketime}")

        elif 'python' in query:
            speak("Okay Sir")
            open_python = "C:\\Program Files\\JetBrains\\PyCharm 2019.2\\bin\\pycharm64.exe"
            os.startfile(open_python)

        elif 'netbeans' in query:
            speak("Okay Sir")
            open_netbeans = "C:\\Program Files\\NetBeans 8.0.1\\bin\\netbeans64.exe"
            os.startfile(open_netbeans)

        elif 'eclips' in query:
            speak("Okay Sir")
            open_eclips = "C:\\Users\\User\\eclipse\\jee - 2019 - 032\\eclipse\\eclipse.exe"
            os.startfile(open_eclips)

        elif 'tor' in query:
            speak("Okay Sir")
            open_eclips = "C:\\Users\\User\\Desktop\\Tor Browser\\Browser\\firefox.exe"
            os.startfile(open_eclips)








