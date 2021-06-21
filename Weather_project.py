# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 02:56:23 2021

@author: lenovo
"""
import sys
import requests
from datetime import datetime

apikey = '1ee32b061f2d8c8f32d1d1a6764e4ffb'
"""Here I have added lowercase function which will return the entered value in lowercase 
even though the user types CAPITAL LETTER as websites does not accept Uppercase"""
location = input("Enter the city name : ").lower()
finallink = 'https://api.openweathermap.org/data/2.5/weather?q='+location+"&appid="+apikey
apilink = requests.get(finallink)
apidata = apilink.json()
directory = "D:/CODING/Spyder/WeatherText/"

#variables to store and display data
temp = ((apidata['main']['temp']) - 273.15)
weather = apidata['weather'][0]['description']
hmdt = apidata['main']['humidity']
windspeed = apidata['wind']['speed']
datetime = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
filepath = directory + input("Enter name to save file as: ")
sys.stdout = open(filepath+".txt", "wt")

print ('----------------------------------------------------------')
print ("Weather Stats for - {} || {}".format(location.upper(), datetime))
print ("----------------------------------------------------------")

print ("Present temperature is     : {:.2f} deg C".format(temp))
print ("Present weather conditions :", weather)
print ("Present humidity status is :", hmdt, '%')
print ("Present wind speed is      :", windspeed, 'kmph')

#END