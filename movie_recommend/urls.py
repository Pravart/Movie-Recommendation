from django.urls import path
from .views import home, recommend_view, search_view

urlpatterns = [
    path("", home),
    path("recommend/", recommend_view),
    path("search/", search_view),   # new endpoint
]
