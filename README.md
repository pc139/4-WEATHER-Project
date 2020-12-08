# 4-WEATHER-Project

### Check the weather! :cloud: 

In this repository you can find a file named ```main.py``` that triggers the Weatherbit.io Weather API, retrieving current weather observations from over 47,000 live weather stations, historical weather data for the past 10 years from the archive of more than 120,000 stations and highly localized weather forecasts for any point in the globe using the world's most trusted weather models!

If you run the program, executing the main file with: ```$ python main.py "Catania" "Italy" 2 -u admin -p admin``` it will  give you results similar to the following: 

```
$ python main.py "Catania" "Italy" 2 -u admin -p admin
In Catania (Italy) the day 2020-12-04 , min temp is 10.1 ,max temp is 16.3 with scattered clouds
```
> **Note:** the project requires the following modules to run: *json, urllib, argparse, hashlib, random, os and squlite3*.

A user can choose an Italian city and the day they need the forecast for. The input city is verified using a function which controls the presence of the chosen location from a csv file containing every Italian town. The input day is an integer with possible values between 1 and 16; it means we are searching for weather information for the n-day, counting from today (day=1 is today, day=2 is tomorrow, and so on).

### Command line parameters :computer:
In order to execute the ```main.py``` file, a few command line parameters must be passed.
#### Positional arguments
- **city**: The city the user needs the temperature forecast for. **Only one** city can be chosen.
- **country**: The city's country the user what the temperature forecast. 
- **day**: The day for which the user wants the temperature forecast. **Only one** day can be chosen.

#### Optional Argument
- **-h, --help**: displays all the possible options for each parameter; 
- **-v**:  displays the output with different levels of verbosity (at the moment only one level of verbosity is supported);
- **-u U [required]:** the username (requires *-p*).  
- **-p P [required]:** the user's password.   
- **--version:** show program's version number and exit.

### How to populate the database :busts_in_silhouette:
In order to run ```main.py``` you will need a **username** and a **password**. The package comes with a **default user** with the following credenentials:
- *username*: **test**
- *password*: **test**

You may want to remove or add new users. You can find a helper module ```dbmanager.py``` in the parent directory that allows you to populate the database.
> **Note:** adding and removing a user at the same time will be **denied** and no actions will be performed on the database.

#### Adding a new user
Use the parameter ```-add```. Requires the following:
 - **-u:** username 
 - **-p:** password
 - **-a:** api key
```
$ python dbmanager.py -add -u test -p test -a 749575cf5a244b2687a26c58849d521c
Successfully inserted user test 
```

#### Removing a user
Use the parameter ```-rm```. Requires the following: 
 - **-u:** username 
```
$ python dbmanager.py -rm -u test
Successfully removed user test
```

### References :green_book:
The API we use is offered by [Weatherbit API](https://www.weatherbit.io/api). With a premium account there is the possibilty to use other specific features. 

### Authors and acknowledgment :busts_in_silhouette:
- **Canovese Pietro**
- **Cavallari Alberto**
- **Rampazzo Francesca**
- **Scattolin Giovanni**

### License :page_facing_up:
[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)

