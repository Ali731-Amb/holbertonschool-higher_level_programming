#!/user/bin/python3

import csv
import json


def convert_csv_to_json(filename_csv):
    try:
        with open(filename_csv, "r", encoding="utf-8") as fcsv:
            reader = csv.DictReader(fcsv)
            liste = list(reader)
            with open("data.json", "w", encoding="utf-8") as fjson:
                json.dump(liste, fjson)
        return True
    except (FileNotFoundError):
        return False
