import json
import urllib
import urllib.request

def min_max_day(api_key, city, country, day):
   """The function queries the Weatherbit.io website in order to obtain the
   forecast information for the users.

   Key arguments:
   api_key - The users' personal api key
   city -- The users' chosen city
   country --- The users' chosen country
   day ---- The users' chosen day
   """

    #api_key = "c34fa0019d8e4461a92ce998d5ee1e11"
    url = "https://api.weatherbit.io/v2.0/forecast/daily?"
    final_url = str(url + "city=" + city + "&country=" + country + "&day"
              + str(day) + "&key=" + api_key)
    final_url = final_url.replace(" ", "%20")
    json_obj = urllib.request.urlopen((final_url))
    js = json.load(json_obj)

    w_info= str("In "+ str(city) + " (" + str(country) + ") " + "the day "
            + str(js["data"][day-1]["datetime"])
            + " , min temp is " +str(js["data"][day-1]["min_temp"])
            + " ,max temp is " + str(js["data"][day-1]["max_temp"]) + " with "
            + str(js["data"][day-1]["weather"]["description"].lower()))
    return w_info, js["lat"], js["lon"]
