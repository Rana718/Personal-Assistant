# neted libary
import wolframalpha
import pyttsx3
import speech_recognition as sr
import datetime 
import wikipedia
import webbrowser
import os
import pyaudio
import pyjokes
import smtplib
import pathlib
import textwrap
import ctypes
import shutil
import sys
import subprocess
import winshell
import requests
import json
import win32com.client as wincl
import google.generativeai as genai
from IPython.display import display
from googletrans import Translator
from gtts import gTTS
from dotenv import load_dotenv


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)
tom = "Tom: "


load_dotenv()
gemini_key = os.getenv('GEMINI_KEY')
open_key = os.getenv('OPEN_KEY')

# list of languages
LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'he': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'ug': 'uyghur',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
}
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.setProperty('rate', 100)

def take_command():
    query = input("User: ")
    return query

def gemini_ai(userd):
    try:
        
        genai.configure(api_key=gemini_key)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(userd)
        gemini = response.text
        final_ans = gemini.replace("*", "")
        print(tom,final_ans)
    except:
        print(tom,"Google Servie Error plase try aging later")

def Tom_reponse():
    print("Tom: ok")

def speech_text():
    recongizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tom: \nSay your speech...")
        audio = recongizer.listen(source)
    try:
        print(tom, recongizer.recognize_google(audio))
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request resluts; {0}".format(e))

def translate_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Bol Bokachoda")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("ok")
        you_text = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"
    return you_text

def translate_text(text, dest_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=dest_language)
    return translated_text.text


class Answer:
    while True:
        query = take_command().lower()
        
        if 'open youtube' in query or 'youtube' in query:
            speak("opening youtube")
            Tom_reponse()
            webbrowser.open("youtube.com")
        elif 'play music' in query or 'play song' in query:
            speak("ok")
            Tom_reponse()
            webbrowser.open("https://youtu.be/wXY3voKbj8M?si=9GXon3Z1g9WX1gfP")
        elif 'how are you' in query:
            speak("i am fine")
            print(tom, "i am fine")
        elif 'what is the time' in query or 'time' in query:
            Time = datetime.datetime.now().strftime("% H:% M:% S")
            speak("time is {Time}")
            print(tom, Time)
        elif 'lock window' in query:
            speak("ok")
            Tom_reponse()
            ctypes.windll.user32.LockworkStsiono()
        elif 'shutdown the system' in query or 'shutdown' in query:
            speak("ok")
            Tom_reponse()
            subprocess.call('shutdown / p / f')
        elif 'weather' in query:
            
            base_url = "https://openweathermap.org/data/2.5/weather?"
            speak("what is your city name")
            print(tom, "Enter your City name")
            city_name = take_command()
            complete_url = base_url+"appid="+open_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            try:
                if x["code"]!="404":
                    y=x["main"]
                    current_temperature = y["temp"]
                    current_pressure = y["pressure"]
                    current_humidity = y["humidity"]
                    z = x["weather"]
                    weather_descripiton = z[0]["description"]
                    print(tom,"Temperature(in kelvin unit)= "+str(current_temperature)+
                        "\n atmospheric pressure(in hpa unit)= "+str(current_pressure)+
                        "\n humidity(in percentage)= "+str(current_humidity)+
                        "\n description = "+str(weather_descripiton))
                else:
                    speak("city not found")
                    print(tom, "Your city is not found")
            except:
                print("sorry!!!")
        elif 'i love you' in query:
            speak("i love you two")
            print(tom, "I Love You 2")
        elif 'exit' in query:
            speak("ok, By")
            print(tom, "BY")
            break
        elif 'speech to text' in query:
            speech_text()
        elif 'translate' in query or 'translate language' in query:
            print(tom,"Enter translate type\n1. text to text\n2. speech to text")
            translate_type = int(input("Tom: Enter your type: "))
            if translate_type == 1:
                text= input("Tom: Enter text to translate: ")
                dest_language = input("Tom: Enter destination language (e.g., 'bn' for bengali, 'hi' for hindi) if you are check the full list so type 'full'\n:")
                if dest_language == "full":
                    print(LANGUAGES)
                    dest_language = input("Tom: Enter destination language")
                
                translated_text = translate_text(text, dest_language)
                engine.say(translated_text)
                print(tom,"Your Translated text is:- ",translated_text)
            elif translate_type == 2:
                text = translate_speech()
                dest_language = input("Tom: Enter destination language (e.g., 'bn' for bengali, 'hi' for hindi) if you are check the full list so type 'full'\n:")
                if dest_language == "full":
                    print(LANGUAGES)
                    dest_language = input("Tom: Enter destination language")
                translated_text = translate_text(text, dest_language)
                engine.say(translated_text)
                print(tom,"Your Translated text is:- ",translated_text)
        else:
            gemini_ai(query)

if __name__ == '__main__':
    clera = lambda: os.system('cls')
    clera()
    Answer()
    
