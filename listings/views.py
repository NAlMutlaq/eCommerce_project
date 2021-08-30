from django.shortcuts import render, get_object_or_404
from .models import Listing


def home(request):
    return render(request, 'home.html')

def index(request):
    listings = Listing.objects.all()
    context = {'listings': listings}
    return render(request, 'listings.html', context)

