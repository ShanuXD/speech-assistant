import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
'''
spi5 is type of api of window! by which we can
use the windows speech method
'''
engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good AfterNoon!")

    else:
        speak("Good Evening!")

    speak("hello i am jarvis, please tell me how can i help you!")

def takeCommand():
    '''
    it take microphone input from user and returns string output
    '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listing...')
        r.pause_threshold=1
        r.energy_threshold=1000
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio,language='en-in')
            print('like you said:',query)
        except Exception as e:
            print("Say that again please..")
            return "None"
        return query

if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak('Accoring to wikipedia')
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'search' in query:
            speak('What do you whant to search for')

        elif 'exit' in query:
            exit()
            pass

