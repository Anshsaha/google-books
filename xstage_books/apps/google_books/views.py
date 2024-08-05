"""This file acts as a starting point for all the main functions
    """

import traceback

from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from utils.utilities import custom_response
from . import services
from django.contrib.auth.decorators import login_required


def login(request):
    try:
        return render(request, "home.html")
    except Exception as err:
        traceback.print_exc()
        return custom_response(message=str(err))


def logout(request):
    try:
        return redirect("/")
    except Exception as err:
        traceback.print_exc()
        return custom_response(message=str(err))


@login_required
def search_books(request):
    try:
        query = request.GET.get("query", "")
        books = services.fetch_books(query) if query else []
        return render(request, "search_books.html", {"books": books, "query": query})
    except Exception as err:
        traceback.print_exc()
        return custom_response(message=str(err))


@login_required
@api_view(["POST"])
def submit_recommendations(request):
    try:
        services.submit_recommendations_service(request.data, request.user.id)
        return custom_response(
            success=True,
            message="Book recommended successfully",
            status=200,
        )
    except Exception as err:
        traceback.print_exc()
        return custom_response(message=str(err))


@login_required
def get_book_recommendations(request):
    try:
        data = services.get_recommendations_service()
        return render(request, "recommendations.html", {"recommendations": data})
    except Exception as err:
        traceback.print_exc()
        return custom_response(message=str(err))


[
    {
        "kind": "books#volume",
        "id": "7PJdzQEACAAJ",
        "etag": "H2ftARIC4kE",
        "selfLink": "https://www.googleapis.com/books/v1/volumes/7PJdzQEACAAJ",
        "volumeInfo": {
            "title": "Name JONA Customized Gift for JONA a Beautiful Personalized",
            "subtitle": "Lined Notebook / Journal Gift, Notebook for JONA,120 Pages, 6 X 9 Inches, Gift for JONA, Personal Diary, JONA, Personalized Journal, Family Notebook, Customized Journal, the Diary Of, First",
            "authors": ["Jona Gift Publishing"],
            "publishedDate": "2019-12-19",
            "description": "Name JONA Customized Gift For JONA A beautiful personalized Notebook Birthday Gift for JONA is a 120 pages Simple and elegant Notebook on a Matte-finish cover, Perfect Journal, Diary, Gift Idea for parents, gradparents, kids, boys, girls, youth and teens. Great for taking notes in class, journal writing and essays, Perfect gift for parents, gradparents, kids, boys, girls, youth and teens as a Birthday gift. 120 pages Size 6 x 9 (15.24 x 22.86 cm)- the ideal size for all purposes, fitting perfectly into your bag White-color paper Soft, glossy cover Matte Finish Cover for an elegant look and feel Looking for on the go notepad for JONA ? Are you looking for a gift for your friend, parents or relatives ? Then you need to buy this Cute Name JONA Customized Gift For JONA A beautiful personalized gift Journal for your brother, sister, Auntie",
            "industryIdentifiers": [
                {"type": "ISBN_10", "identifier": "1677532300"},
                {"type": "ISBN_13", "identifier": "9781677532308"},
            ],
            "readingModes": {"text": False, "image": False},
            "pageCount": 122,
            "printType": "BOOK",
            "maturityRating": "NOT_MATURE",
            "allowAnonLogging": False,
            "contentVersion": "preview-1.0.0",
            "panelizationSummary": {
                "containsEpubBubbles": False,
                "containsImageBubbles": False,
            },
            "imageLinks": {
                "smallThumbnail": "http://books.google.com/books/content?id=7PJdzQEACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api",
                "thumbnail": "http://books.google.com/books/content?id=7PJdzQEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api",
            },
            "language": "en",
            "previewLink": "http://books.google.co.in/books?id=7PJdzQEACAAJ&dq=jona&hl=&cd=1&source=gbs_api",
            "infoLink": "http://books.google.co.in/books?id=7PJdzQEACAAJ&dq=jona&hl=&source=gbs_api",
            "canonicalVolumeLink": "https://books.google.com/books/about/Name_JONA_Customized_Gift_for_JONA_a_Bea.html?hl=&id=7PJdzQEACAAJ",
        },
        "saleInfo": {"country": "IN", "saleability": "NOT_FOR_SALE", "isEbook": False},
        "accessInfo": {
            "country": "IN",
            "viewability": "NO_PAGES",
            "embeddable": False,
            "publicDomain": False,
            "textToSpeechPermission": "ALLOWED",
            "epub": {"isAvailable": False},
            "pdf": {"isAvailable": False},
            "webReaderLink": "http://play.google.com/books/reader?id=7PJdzQEACAAJ&hl=&source=gbs_api",
            "accessViewStatus": "NONE",
            "quoteSharingAllowed": False,
        },
        "searchInfo": {
            "textSnippet": "Name JONA Customized Gift For JONA A beautiful personalized Notebook Birthday Gift for JONA is a 120 pages Simple and elegant Notebook on a Matte-finish cover, Perfect Journal, Diary, Gift Idea for parents, gradparents, kids, boys, girls, ..."
        },
    }
]
