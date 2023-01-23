from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
  

def index(request):
    now = datetime.now()

    return render(
        request,
        "Landing_Page/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'title': "HypeSpace",
            'content': " on " + now.strftime("%A, %d %B, %Y at %X"),
            'message': "Successful Launch!",
        }
    )

def about(request):
    return render(
        request,
        "Landing_Page/about.html",
        {
            'title': "About HelloDjangoApp",
            'content': "Example app page for Django."
        }
    )