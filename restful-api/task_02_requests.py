#!/usr/bin/python3

"""
Fetch and process posts from a REST API.
Provides print and CSV export functions.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch posts and print their titles from the API.
    """
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status code : {r.status_code}")

    if r.status_code == 200:
        obj = r.json()
        for item in obj:
            print(item["title"])


def fetch_and_save_posts():
    """
    Fetch posts and save them to a CSV file.
    """
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status code : {r.status_code}")

    if r.status_code == 200:
        obj = r.json()
        p = []
        for item in obj:
            post_dict = {
                "id": item["id"],
                "title": item["title"],
                "body": item["body"]
                }
            p.append(post_dict)

            fieldnames = ["id", "title", "body"]
        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(p)
