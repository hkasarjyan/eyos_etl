import csv
import errno
from os import strerror

from db.crud import get_country_by_name
from models import Stores


class CSVread:
    filtered = []

    def __init__(self, file):
        self.file = file
        self.reader = []

    def get_file(self):
        try:
            with open(self.file, "r") as f:
                self.reader = [row for row in csv.reader(f, delimiter=",")]
                self.reader = self.reader[1:]
                return self.reader
        except IOError as err:
            print("I/O error({0}): {1}".format(errno, strerror))
        return

    def get_num_rows(self):
        return len(self.reader)


def make_first_letter_upper(my_string):
    return my_string.capitalize()


def get_store_from_csv(csv_line) -> Stores:
    store = Stores()
    store.store_name = csv_line[0]
    store.country_code = get_country_by_name(
        make_first_letter_upper(csv_line[1])
    ).country_code

    store.street_name = csv_line[2]
    store.pin_code = csv_line[3]
    store.lvl1_geog = csv_line[4]
    store.lvl2_geog = csv_line[5]
    store.lvl3_geog = csv_line[6]

    return store
