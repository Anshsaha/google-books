"""This file will contain all the url endpoints for the APIs
    """

from django.urls import path
from . import views

urlpatterns = [
    # path("", views.HealthCheckView.as_view(), name="health-check"),
    path("", views.login, name="login"),
    path("search/", views.search_books, name="search_books"),
    path(
        "submit_recommendation/",
        views.submit_recommendations,
        name="submit_recommendation",
    ),
    # path("thank-you/", thank_you_view, name="thank_you"),
    path(
        "get-recommendations/",
        views.get_book_recommendations,
        name="get_recommendation",
    ),
]
