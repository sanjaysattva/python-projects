import requests

Base_url = "https://api.openweathermap.org/data/2.5/weather?"
API_key = "32ba1ac3f4d89a6d7d4a35a7f6f35da1" #api key
city = "Chennai"

def conversion(temp):
  celcius = temp-273
  farenheit = celcius*(9/5) + 32
  return celcius,farenheit #return as a tuple

url = Base_url+"appid="+API_key+"&q="+city #concatenating the url of api

weather = requests.get(url).json()  #weather is a dictionary of dictionaries in json format

temp = weather['main']['temp']#obtain particular data using dictionary key words
temp_c , temp_f = conversion(temp)
humidity = weather['main']['humidity']
climate = weather['weather'][0]['description']#'weather is a list of dictionaries , even though it has only one dictionary in it
print("Temperature :")
print(temp_c,"or",temp_f)
print(f"humidity in {city} is {humidity}% and climate is {climate}")



print(weather)

