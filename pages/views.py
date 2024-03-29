from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from . models import Client
from listings.choices import price_choices, bedroom_choices, state_choices
# Create your views here.


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    clients = Client.objects.order_by('-date_added')[:4]
    context = {
        'listings': listings,
        'clients': clients,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get Seller of the month (MVP)
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)
