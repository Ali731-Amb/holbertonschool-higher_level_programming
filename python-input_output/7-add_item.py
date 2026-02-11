#!/usr/bin/python3
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
if __name__ == "__main__":
    _argv = sys.argv[1:]
    try:
        ma_liste = load_from_json_file("add_item.json")
    except FileNotFoundError:
        ma_liste = []
    ma_liste.extend(_argv)
    save_to_json_file(ma_liste, "add_item.json")
