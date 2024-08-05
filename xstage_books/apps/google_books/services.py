"""This file contains all the main content of each api
    """

import requests
import time
import os
from apps.google_books.models import BookRecommendation

GOOGLE_BOOKS_API_URL = os.getenv("GOOGLE_BOOKS_API_URL")


def fetch_books(query, max_results=10):
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


def submit_recommendations_service(request):
    BookRecommendation.objects.create(
        title=request.data["title"],
        author=request.data["author"],
        user_id=request.user.id,
    )


def get_recommendations_service():
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


def fetch_book_details(title, author):
    print(title, author)
    params = {
        "q": f"intitle:{title}+inauthor:{author}",
        "key": os.getenv("API_KEY"),
    }
    response = requests.get(GOOGLE_BOOKS_API_URL, params=params)
    print(response.status_code)
    data = response.json()
    items = data.get("items", [])

    if items:
        return items[0]

    return None
