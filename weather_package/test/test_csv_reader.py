import os
import unittest

from weather_package.scripts.csv_reader import read_store_user_data


class TestCSVReader(unittest.TestCase):
    """This class applies some unittest functionalities to
    the read_store_user_data function.
    """

    # setUp function prepare some data for tests
    def setUp(self):
        # create an empty file
        self.temporary_file = 'temporary_file'
        f = open(self.temporary_file, 'w')
        f.close()


    def test_no_datafile(self):
        df = read_store_user_data('thisfiledoesnotexist')
        self.assertFalse(df)

    def test_empty_datafile(self):
        df = read_store_user_data(self.temporary_file)
        self.assertFalse(df)

    def test_file_is_not_csv(self):
        df = read_store_user_data(self.temporary_file)
        self.assertFalse(df)

    # tearDown function cleans the temporary data
    def tearDown(self):
        os.remove(self.temporary_file)


if __name__ == "__main__":
    unittest.main(verbosity=2)
