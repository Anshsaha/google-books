"""This file contains all the main content of each api
    """

import requests
import time
import os
from apps.google_books.models import BookRecommendation

GOOGLE_BOOKS_API_URL = os.getenv("GOOGLE_BOOKS_API_URL")


def fetch_books(query: str, max_results: int = 10) -> list:
    """This function fetches all the results according to the query

    Args:
        query (str): search keyword given by the user.
        max_results (int, optional): Defaults to 10.

    Returns:
        list: Metadata of all the resultant books.
    """
    params = {
        "q": query,
        "maxResults": max_results,
        "key": os.getenv("API_KEY"),
    }
    response = requests.get(GOOGLE_BOOKS_API_URL, params=params)
    if response.status_code == 429:
        time.sleep(10)
        response = requests.get(GOOGLE_BOOKS_API_URL, params=params)
    return response.json().get("items", [])


def submit_recommendations_service(data: dict, user_id: int) -> None:
    """This function creates a record of recommendation given by the user

    Args:
        data (dict): metadata of the books recommended by the user.
        user_id (int): user id
    """
    BookRecommendation.objects.create(
        title=data["title"],
        author=data["author"],
        user_id=user_id,
    )


def get_recommendations_service() -> list:
    """This function gets the overall recommendations data.

    Returns:
        list: metadata of all the recommendations
    """
    recommendations = BookRecommendation.objects.all().order_by("-created_at")
    book_details = []
    for rec in recommendations:
        book_data = fetch_book_details(rec.title, rec.author)
        if book_data:
            book_details.append(
                {
                    "id": rec.id,
                    "user_name": rec.user.username,
                    "title": rec.title,
                    "author": rec.author,
                    "created_at": rec.created_at,
                    "google_books_info": book_data,
                }
            )

    return book_details


def fetch_book_details(title: str, author: str) -> list:
    """This function fetches the data from google books api
    according to the records existing in the database.

    Args:
        title (str): title of the book
        author (str): author of the book

    Returns:
        list: metadata of each book
    """
    params = {
        "q": f"intitle:{title}+inauthor:{author}",
        "key": os.getenv("API_KEY"),
    }
    response = requests.get(GOOGLE_BOOKS_API_URL, params=params)
    data = response.json()
    items = data.get("items", [])

    if items:
        return items[0]

    return None
