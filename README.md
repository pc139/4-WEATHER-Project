# 4-WEATHER-Project

## Check the weather! :cloud: 

In this repository you can find a file named ```main.py``` that triggers the Weatherbit.io Weather API, retrieving current weather observations from over 47,000 live weather stations, historical weather data for the past 10 years from the archive of more than 120,000 stations, and highly localized weather forecasts for any point on the globe using the world's most trusted weather models!

If you run the program, executing the main file with: ```$ python main.py ``` it will  give you results similar to the following: 

```
$ python main.py "Catania" "Italy" 2  
In Catania (Italy) the day 2020-12-04 , min temp is 10.1 ,max temp is 16.3 with scattered clouds
```
> **Note:** the project requires the following modules to run: *json, urllib*.

A user can choose an Italian city and the day they need the forecast for. The city is selected using a function which pulls the chosen location from a csv file containing every Italian town. The input day is an integer with possible values between 1 and 16; it means we are searching for weather information for the n-day, counting from today (day=1 is today, day=2 is tomorrow, and so on).



### References :green_book:
The API we use is offered by [Weatherbit API](https://www.weatherbit.io/api). With a premium account there is the possibilty to use other specific features. 

### Authors and acknowledgment :busts_in_silhouette:
- **Canovese Pietro**
- **Cavallari Alberto**
- **Rampazzo Francesca**
- **Scattolin Giovanni**

### License :page_facing_up:
[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)

