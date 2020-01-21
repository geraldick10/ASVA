from __future__ import print_function
import datetime
import pickle
import os.path
from selenium import webdriver
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import speech_recognition as sr
from gtts import gTTS
import os
import random
from time import ctime
import time
import playsound
import subprocess
import webbrowser
import wikipedia
import sys
import socket



r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        print('say something')
        audio = r.listen(source)
        voice_data ='weather'
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            asva_speak('sorry sir i didnt get that')
        except sr.RequestError:
            asva_speak('sorry my service is down')
        
        return voice_data


def asva_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'hello' in voice_data:
        asva_speak('halo sir,my name is Asva your virtual assistant')
    if 'what is your name' in voice_data:
        asva_speak('my name is Asva')
    if 'what time is it' in voice_data:
        asva_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('what do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        asva_speak('here is what i found for '+ search +' sir')
    if 'find location' in voice_data:
        location = record_audio('what is the location sir?')
        url = 'https://google.nl/maps/place/' + location + '/&amp'
        webbrowser.get().open(url)
        asva_speak('here is the location of '+ location +' sir')
    if 'goodbye' in voice_data:
        asva_speak('have nice day sir')
        exit()
    if 'find' in voice_data:
        wiki = record_audio('what can i search for you?')
        asva_speak('in my information in wikipedia' + wiki +'is')
        content = (wikipedia.summary(wiki,sentences=2))
        asva_speak(content)
    if 'look' in voice_data:
        video = record_audio('what can i search for you in youtube?')
        url = 'https://www.youtube.com/results?search_query=' + video
        asva_speak('here is what i found for' + video +'in youtube')
        webbrowser.get().open(url)
    if 'my location' in voice_data:
        url = 'https://www.google.com/maps/search/my+location/@-7.3163051,112.7200749,15z'
        webbrowser.get().open(url)
        asva_speak('here is your location ' + ' sir')
    if 'shutdown' in voice_data:
        asva_speak('yes sir,your computer will shut down in,,3,,2,,1')
        asva_speak('goodbye sir,have a nice day')
        url = 'C:/python37/project/voice assistant/shut.bat'
        webbrowser.get().open(url)
        os.system('shut.bat')
    if 'log off' in voice_data:
        asva_speak('yes sir,your computer will log off in,,3,,2,,1')
        asva_speak('goodbye sir,have a nice day')
        url = 'C:/python37/project/voice assistant/log_off.bat'
        webbrowser.get().open(url)
        os.system('log_off.bat')
    if 'restart' in voice_data:
        asva_speak('yes sir,your computer will restart in,,3,,2,,1')
        asva_speak('goodbye sir,have a nice day')
        url = 'C:/python37/project/voice assistant/restart.bat'
        webbrowser.get().open(url)
        os.system('restart.bat')
    if 'weather' in voice_data:
        driver = webdriver.Chrome()
        city = record_audio('where is the city sir?')
        driver.get("https://weather-forecast.com/locations/"+city+"/forecasts/latest")
        asva_speak('in my information weather in'+city+'is')
        asva_speak(driver.find_elements_by_class_name("b-forecast__table-description-content")[0].text)
        # webbrowser.get().open(url)
        # asva_speak('here is the location of '+ location +' sir')


time.sleep(1)
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        asva_speak('good Morning sir!')
    if hour>=12 and hour<18:
        asva_speak('good Afternoon sir!')
    if hour>=18 and hour<0:
        asva_speak('good night sir!')
wishMe()
asva_speak('iam asva,your virtual assistant,how can i help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)

