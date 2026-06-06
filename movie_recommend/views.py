from django.shortcuts import render
from django.http import JsonResponse
from .ml_code import recommend, search_movies

def home(request):
    return render(request, "index.html")

def recommend_view(request):
    movie = request.GET.get("movie")
    if not movie:
        return JsonResponse({"error": "No movie provided"}, status=400)
    recs = recommend(movie)
    return JsonResponse({"recommendations": recs})

def search_view(request):
    query = request.GET.get("q")
    if not query:
        return JsonResponse({"error": "No query provided"}, status=400)
    results = search_movies(query)
    return JsonResponse({"matches": results})
