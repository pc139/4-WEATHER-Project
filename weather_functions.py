import json
import urllib
import urllib.request

def min_max_day(city, country, day):

    api_key = "c34fa0019d8e4461a92ce998d5ee1e11"
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
    return w_info
