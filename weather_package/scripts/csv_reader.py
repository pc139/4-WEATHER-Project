import pandas as pd
import argparse


def read_store_user_data(results_path):
    """Create a pandas dataframe with information stored in the csv file
    located in result_path, handling some exceptions errors.
    If this module is launched directly it prints some information about
    the last user query.
    """

    try:
        # Storing information about towns in a pandas dataframe
        user_data = pd.read_csv(results_path, sep=',', header=0)
    except FileNotFoundError:
        print ('The file does not exist')
        return

    except ValueError:
        print ('File has a wrong encoding')
        return

    except UnicodeDecodeError:
        print ('File has a wrong encoding')
        return

    print ('The last user launched the program on: ',
           str((user_data['datetime'].iloc[-1])[0:19]),
           ', searching weather information for: ',
           str(user_data['city'].iloc[-1]))


if __name__ == '__main__':
    results_path = 'weather_package/data/outputs.csv'
    read_store_user_data(results_path)
