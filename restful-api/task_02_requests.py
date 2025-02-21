#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()
        data = [
            {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            for post in posts
        ]

        # Écriture dans un fichier CSV
        with open("posts.csv", mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(data)


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
