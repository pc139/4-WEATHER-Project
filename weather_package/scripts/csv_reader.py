import pandas as pd
import argparse

def read_store_user_data (results_path):

    """Read the file containing users' queries, store it in a DataFrame
    :param path: The path to the .csv file containing the information about the queries of all users
    :type path: string
    :return: the Dataframe containing users' queries
    :rtype: Pandas.Dataframe
    """

    try:
        # Storing information abount cities
        user_data = pd.read_csv(results_path, sep=",", header=0)


    except FileNotFoundError:
        print("The file does not exist")
        return

    except ValueError:
        print("File has a wrong encoding")
        return

    except UnicodeDecodeError:
        print("File has a wrong encoding")
        return

    print ("The last user launched the program on: ", str(user_data['datetime'].iloc[-1][0:19]),
           ", searching weather information for: ", str(user_data['city'].iloc[-1]))

if __name__ ==  "__main__":
    results_path = 'weather_package/data/outputs.csv'
    read_store_user_data(results_path)

