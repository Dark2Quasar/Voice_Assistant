import datetime
import speech_recognition as sr
import webbrowser
import urllib
import pyttsx3
import wikipedia


def speak(audio):
    engine = pyttsx3.init('sapi5')
    engine.say(audio)
    engine.runAndWait()
    engine.stop()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir.")
       
    elif hour > 12 and hour < 17:
        speak("Good Afternoon sir.")
        
    else:
        speak("Good Evening sir.")
    speak("I am Assistor , and I assist you for your query, Just Ask.")
    speak("When you're done say close.")
    
def takeCommand():

    '''It takes microphone input from the user and respond in favour of command received.'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")


    except Exception as e:
        print("I couldn't hear that, Please speak again...")
        return "None"
    return query

def search_web(query):
    query = urllib.parse.quote_plus(query)
    url = f"https://www.google.com/search?q={query}"
    speak(f"searchig for {query} on Google.")
    webbrowser.open(url)

def searchYouTube(query):
    query = urllib.parse.quote_plus(query)
    url = f"https://www.youtube.com/search?q={query}"
    speak(f"searchig for {query} on YouTube.")
    webbrowser.open(url)
   

if __name__ == "__main__":
    wishMe()
    
#Task Executing Logic.  
while True:
    query = takeCommand().lower()

    if "wikipedia" in query:
        speak("Searching wikipedia...")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query)
        speak("According to wikipedia.")
        print(results)
        speak(results)
    elif "open youtube" in query:
        speak("opening youtube.")
        webbrowser.open("youtube.com")

    elif "open google" in query:
        speak("opening google.")
        webbrowser.open("google.com")

    elif "open instagram" in query:
        speak("opening instagram.")
        webbrowser.open("instagram.com")

    elif "open facebook" in query:
        speak("opening Facebook.")
        webbrowser.open("facebook.com")

    elif "open roblox" in query:
        speak("Opening Roblox.")
        webbrowser.open("https://www.roblox.com/share?code=bde51987281f0045a5fdd4fd26cd5a25&type=Profile&source=ProfileShare&stamp=1758718838602")

    elif "search for" in query:
        speak("Searching on Google, Please wait.")
        query = query.replace("search for","")
        search_web(query)

    elif "search youtube" in query:
        speak("Searching on YouTube, Please wait.")
        query = query.replace("search youtube","")
        searchYouTube(query)
        

    elif "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"Sir, the time is: {strTime}")        
        

    if query in ["exit","close","quit"]:
        speak('Program Exited Sucessfully, Thanks for your time.')
        break

        
                    
       

