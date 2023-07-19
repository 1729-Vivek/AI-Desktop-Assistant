import speech_recognition as sr
import os
import webbrowser
import subprocess
import datetime
import psutil
def say(text):
    os.system(f"espeak '{text}'")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = r.listen(source)
            print("Recognizing.....")
            query = r.recognize_google(audio, language="en-IN")  # hi-IN or kn-IN for Kannada
            print(f"User said: {query}")
            return query.lower()  # Convert the query to lowercase to handle case-insensitivity
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            return None
        except sr.RequestError as e:
            print(f"Error connecting to Google API: {e}")
            return None
def is_camera_running():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'cheese':
            return True
    return False

if __name__ == '__main__':
    print('PyCharm')
    say("Hello I am Jarvis AI")
    camera_opened = False  # Variable to keep track of whether the camera is opened or not
    while True:
        print("Listening....")
        query = takeCommand()
        if query is not None:
            sites = [
                ["youtube", "https://www.youtube.com"],
                ["wikipedia", "https://www.wikipedia.org"],
                ["o rangrez", "https://www.youtube.com/watch?v=5idNBcKDtvA&list=RD5idNBcKDtvA&start_radio=1"],
                ["google", "https://www.google.com"],
                ["github", "https://www.github.com"],
                ["reddit", "https://www.reddit.com"],
                ["stackoverflow", "https://stackoverflow.com"],
                ["amazon", "https://www.amazon.com"],
                ["facebook", "https://www.facebook.com"],
                ["twitter", "https://www.twitter.com"],
                ["linkedin", "https://www.linkedin.com"],
                ["instagram", "https://www.instagram.com"],
                ["netflix", "https://www.netflix.com"],
                ["yahoo", "https://www.yahoo.com"],
                ["Despacito", "https://www.youtube.com/watch?v=kJQP7kiw5Fk"],
                ["Shape of You", "https://www.youtube.com/watch?v=JGwWNGJdvx8"],
                ["Believer", "https://www.youtube.com/watch?v=7wtfhZwyrcc"],
                ["See You Again", "https://www.youtube.com/watch?v=RgKAFK5djSk"],
                ["Uptown Funk", "https://www.youtube.com/watch?v=OPf0YbXqDm0"],
                ["Chaiyya Chaiyya", "https://www.youtube.com/watch?v=WSneyYMkkHw"],
                ["Tum Hi Ho", "https://www.youtube.com/watch?v=IUOE7eYXKR0"],
                ["Kabira", "https://www.youtube.com/watch?v=jHNNMj5bNQw"],
                ["Ghungroo", "https://www.youtube.com/watch?v=qFkNATtc3mc"],
                ["Dil Diyan Gallan", "https://www.youtube.com/watch?v=SAcpESN_Fk4"],
                # Add more Hindi songs here...
                ["BBC News", "https://www.bbc.com/news"],
                ["CNN", "https://edition.cnn.com/"],
                ["The New York Times", "https://www.nytimes.com/"],
                ["The Guardian", "https://www.theguardian.com/"],
                ["Reuters", "https://www.reuters.com/"],
                ["Al Jazeera", "https://www.aljazeera.com/"],
                ["Hindustan Times", "https://www.hindustantimes.com/"],
                ["The Times of India", "https://timesofindia.indiatimes.com/"],
                ["NDTV", "https://www.ndtv.com/"],
                # Add more news websites here...
                ["National Geographic", "https://www.nationalgeographic.com/"],
                ["NASA", "https://www.nasa.gov/"],
                ["IMDb", "https://www.imdb.com/"],
                ["TED", "https://www.ted.com/"],
                ["Wolfram Alpha", "https://www.wolframalpha.com/"],
                ["Unsplash", "https://unsplash.com/"],
                ["Etsy", "https://www.etsy.com/"],
                ["Instructables", "https://www.instructables.com/"],
                ["TV Tropes", "https://tvtropes.org/"],
                ["Food Network", "https://www.foodnetwork.com/"],
                ["GIPHY", "https://giphy.com/"],
                ["The Verge", "https://www.theverge.com/"],
                # Add more interesting websites/topics here...
                ["ChatGPT Playground", "https://platform.openai.com/"],
                ["ChatGPT API", "https://beta.openai.com/signup/"],
                ["ISRO", "https://www.isro.gov.in/"],
                ["NASA", "https://www.nasa.gov/"],
                ["PARENT LOGIN","parent-login.nmamit.in"],
                ["MOODLE","guru.nmamit.in/my/"],
            ]

            for site in sites:
                if f"open {site[0]}".lower() in query:  # Modify the condition to use "open" before the site name
                    say(f"Opening {site[0]} sir....")
                    webbrowser.open(site[1])

            if "open music" in query:
                musicPath = "/home/vats/Downloads/song.mp3"
                os.system(f"open {musicPath}")

            if "the time" in query:
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"Sir the time is {strfTime}")

            if "time is" in query:
                hour = datetime.datetime.now().strftime("%H")
                min = datetime.datetime.now().strftime("%M")
                sec = datetime.datetime.now().strftime("%S")
                say(f"Sir time is {hour} baj ke {min} minutes {sec} second huaa hai")

            if "thank you" in query and "jarvis" in query:  # Check for both "thank you" and "jarvis" in the query
                say("It's my pleasure sir")

            if "open camera" in query:  # Use all lowercase for easier recognition
                subprocess.Popen(["cheese"])  # Run the camera opening process in the background
                camera_opened=True

            if "open brave browser" in query:
                subprocess.Popen(["/usr/bin/brave-browser"])

            if "close camera" in query and camera_opened:  # Check for "close camera" only if camera is opened
                if is_camera_running():
                    os.system("killall cheese")  # Terminate the "cheese" process
                camera_opened = False  # Set camera_opened to False

            if "stop" in query or "exit" in query:
                say("Goodbye sir. Exiting.")
                break
