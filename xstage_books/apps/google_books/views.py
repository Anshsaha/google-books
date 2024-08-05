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
