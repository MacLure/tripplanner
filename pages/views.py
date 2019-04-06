from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def trips_view(request, *args, **kwargs):
    my_context = {
        "my_text": "this is some text",
        "my_number": 123
    }
    return render(request, "trips.html", my_context)
