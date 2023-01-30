# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 23:34:17 2023

@author: joebl
"""

import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer()

while True:
    
    try:
        
        with speech_recognition.Microphone() as mic:
            
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            
            text = recognizer.recognize_google(audio)
            text = text.lower()
            
            print('Recognized {}'.format(text))

    
    except Exception as e:
        
        print(e)
        