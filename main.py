import speech_recognition as sr
import os
import webbrowser
import subprocess
import re
import openai
from config import apikey
import datetime
import psutil
import random
import pyowm
from newsapi import NewsApiClient
# Initialize News API Client
newsapi = NewsApiClient(api_key='98e9089378384856834740a199781a7c')

# Initialize OpenWeatherMap Client
owm = pyowm.OWM('268ac7a59030442dbaa05331232507')

def get_weather(city):
    try:
        # Search for the city in OpenWeatherMap
        observation = owm.weather_at_place(city)
        w = observation.get_weather()

        # Get weather details
        weather_status = w.get_status()
        temperature = w.get_temperature('celsius')['temp']
        humidity = w.get_humidity()

        say(f"The weather in {city} is {weather_status}.")
        say(f"The temperature is {temperature:.1f} degrees Celsius.")
        say(f"The humidity is {humidity}%.")
    except pyowm.exceptions.api_response_error.NotFoundError:
        say(f"Sorry, I couldn't find weather information for {city}.")
    except pyowm.exceptions.api_call_error.APICallError:
        say("Sorry, there was an error while fetching the weather information.")

# Example usage

def play_youtube_song(song_name):
    # Use regular expressions to remove any unwanted words like "play", "song", etc. from the user's query
    song_name = re.sub(r'play|song', '', song_name, flags=re.IGNORECASE).strip()

    # Construct the YouTube URL for the song search
    youtube_url = f"https://www.youtube.com/results?search_query={song_name}"

    # Open the URL in the default web browser
    webbrowser.open(youtube_url)
    say(f"Playing {song_name} on YouTube.")

def get_top_headlines():
    # Get top headlines from News API
    top_headlines = newsapi.get_top_headlines(language='en', country='us', page_size=5)

    # Extract and read the news titles
    if top_headlines['status'] == 'ok':
        articles = top_headlines['articles']
        for index, article in enumerate(articles):
            title = article['title']
            say(f"News {index + 1}: {title}")
    else:
        say("Sorry, I couldn't fetch the latest news at the moment.")




chatStr= ""
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key=apikey
    chatStr+=f"Vivek: {query}\n Jarvis:"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response["choices"][0]["text"])
    chatStr+=f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


    
def ai(prompt):
    openai.api_key = apikey
    text= f"OpenAi response for prompt: {prompt} \n ***************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        print(response["choices"][0]["text"])
        text+=response["choices"][0]["text"]
        if not os.path.exists("OpenAi"):
            os.mkdir("OpenAi")

        with open(f"OpenAi/prompt -{random.randint(1,123456789)}","w") as f:
            f.write(text)
    except KeyError as e:
        # This block will execute if the "choices" key or the index 0 is not found in the response dictionary.
        print("An error occurred while accessing the 'choices' key or index 0.")
        print(f"Error message: {e}")
    except Exception as e:
        # This block will catch any other unexpected exceptions that may occur during the print statement.
        print("An unexpected error occurred.")
        print(f"Error message: {e}")


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

            if "open music  man meri jaan" in query:
                musicPath = "/home/vats/Downloads/song.mp3"
                os.system(f"open {musicPath}")

            elif "the time" in query:
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"Sir the time is {strfTime}")

            elif "time is" in query:
                hour = datetime.datetime.now().strftime("%H")
                min = datetime.datetime.now().strftime("%M")
                sec = datetime.datetime.now().strftime("%S")
                say(f"Sir time is {hour} baj ke {min} minutes {sec} second huaa hai")

            elif "thank you" in query and "jarvis" in query:  # Check for both "thank you" and "jarvis" in the query
                say("It's my pleasure sir")

            elif "open camera" in query:  # Use all lowercase for easier recognition
                subprocess.Popen(["cheese"])  # Run the camera opening process in the background
                camera_opened=True

            elif "open brave browser" in query:
                subprocess.Popen(["/usr/bin/brave-browser"])

            elif "latest news" in query.lower():
                get_top_headlines()

            elif "close camera" in query and camera_opened:  # Check for "close camera" only if camera is opened
                if is_camera_running():
                    os.system("killall cheese")  # Terminate the "cheese" process
                camera_opened = False  # Set camera_opened to False

            elif "Using artificial intelligence".lower() in query.lower():
                ai(prompt=query)

            elif "weather in" in query.lower():
                city = query.lower().split("weather in")[1].strip()
                get_weather(city)

            elif "play a song" in query.lower():
            # Extract the song name from the user's query and play it on YouTube
                song_name = query.lower().replace("play a song", "").strip()
                play_youtube_song(song_name)

            elif "stop" in query or "exit" in query:
                say("Goodbye sir. Exiting.")
                break

            else:
                print("Chatting")
                chat(query)