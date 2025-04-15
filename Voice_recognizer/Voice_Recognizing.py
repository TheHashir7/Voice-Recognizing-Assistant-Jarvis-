import pyttsx3
import webbrowser
import datetime
import os
import wikipedia
import speech_recognition as sr


engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
# engine Voice can change to male or female 0 or 1 
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetings():
    hours=int(datetime.datetime.now().hour)
    if hours>=0 and hours<=12:
        speak("Good Morning")
    elif hours>=12 and hours<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Jarvis Sir. Please tell me how may I help you")  

# User speak and this will recognize the command
def take_command():
    s=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        # Voice if user stop for sec in pause then it will process the audio
        s.pause_threshold=2
        audio = s.listen(source)
    try:
        print("Recognizing....")
        query = s.recognize_google(audio, language="en-US")
        print(f"User said {query}\n")
    except Exception as e:
        print("Say that again please")
        return "None"
    return query

if __name__=="__main__":
    greetings()

    while True:
        query = take_command().lower()
        if "wikipedia" in query:
            speak("Searching wikipedia....")
            query = query.replace("wikipedia", "")
            result=wikipedia.summary(query,sentences=2)
            speak("Acording to wikipidia....")
            print(result)
            speak(result)
# Easy browsing
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open facebook" in query:
            webbrowser.open("facebook.com")
        elif "open twitter" in query or "open x" in query:
            webbrowser.open("https://x.com")
        elif "open gpt" in query or "open chat gpt" in query:
            webbrowser.open("chatgpt.com")
        elif "open linkedin" in query:
            webbrowser.open("linkedin.com")

        elif " what is the time" in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {time}")

        elif "play music" in query:
            folder="D:\Music"
            song=os.listdir(folder)
            print(song)
            os.startfile(os.path.join(folder, song[0]))

        elif "open code" in query:
            to_code="E:\VS Code\Microsoft VS Code"
            os.startfile(to_code)
        else:
            print("No query matched")