import weather_functions

if __name__ == "__main__":
    temps = weather_functions.min_max_day("Catania", "Italy", 1)
    print(temps)
