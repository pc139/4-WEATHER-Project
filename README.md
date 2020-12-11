# 4-WEATHER-Project

### Check the weather! :partly_sunny: 

In this repository you can find a file named ```main.py``` that triggers the Weatherbit.io Weather API, retrieving current weather observations from over 47,000 live weather stations, historical weather data for the past 10 years from the archive of more than 120,000 stations and highly localized weather forecasts for any point in the globe using the world's most trusted weather models!

If you run the program, executing the main file with: ```$ python main.py "Catania" "Italy" 2 -u admin -p admin``` it will  give you results similar to the following: 

```
$ python main.py "Catania" "Italy" 2 -u admin -p admin
In Catania (Italy) the day 2020-12-04 , min temp is 10.1 ,max temp is 16.3 with scattered clouds
```
> **Note:** the project requires the following modules to run: *json, urllib, argparse, hashlib, random, os and squlite3*.

A user can choose an Italian city and the day they need the forecast for. The input city is verified using a function which controls the presence of the chosen location from a csv file containing every Italian town. The input day is an integer with possible values between 1 and 16; it means we are searching for weather information for the n-day, counting from today (day=1 is today, day=2 is tomorrow, and so on). Once a user has asked for a forecast, their information will be registered in a csv file named outputs.csv, along with the exact time they queried their request. This is done through an internal function in the csv_manager.py.

### Data Files :file_folder:
The complete list of Italian towns names is stored in a csv file located in
 ```weather_package/data/comuni_italiani.csv```. <br>
This file contains the names of 7978 Italian towns. The following table represents the first five rows of our csv file
 
|    id        |    comune             | istat   | provincia |
|--------------|-----------------------|---------|-----------|
|	 1         | Abano Terme           | 28001   | Padova    |
|	 2         | Abbadia Cerreto       | 98001   | Lodi      |
|	 3         | Abbadia Lariana       | 97001   | Lecco     |
|	 4         | Abbadia San Salvatore | 52001   | Siena     |
|	 5         | Abbasanta             | 95001   | Oristano  |

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
$ python dbmanager.py -add -u admin -p admin -a 749575cf5a244b2687a26c58849d521c
Successfully inserted user admin 
```

#### Removing a user
Use the parameter ```-rm```. Requires the following: 
 - **-u:** username 
```
$ python dbmanager.py -rm -u admin
Successfully removed user admin
```

#### Displaying all the users
Use the parameter ```-ds```. Requires the following: 
 - **-u:** username 
 - **-p:** password
```
$ python dbmanager.py -ds -u admin -p admin
Users' list:
admin
```

#### Get last user query information
Access datetime and city of the last user query to our program are provided by running:
```
$ python weather_package\scripts\csv_reader.py
The last user launched the program on:  2020-12-10 22:45:11 , searching weather information for:  Milano
```

### Testing :ballot_box_with_check:
Tests on parts of the code are provided here: weather_package/test/ .
Here you can find a module named ```test_csv_reader.py```.
To run them use: ```python -m unittest -v -b weather_package/tests/test_csv_reader.py```:

```
test_empty_datafile (weather_package.tests.test_csv_reader.TestCSVReader) ... ok
test_file_is_not_csv (weather_package.tests.test_csv_reader.TestCSVReader) ... ok
test_no_datafile (weather_package.tests.test_csv_reader.TestCSVReader) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.040s

OK
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

