from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from listings.models import Band
from listings.models import Title


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html',
                  {'bands': bands})


def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html',
                  {'band': band})


def about(request):
    return render(request, 'listings/about.html')


def listings_list(request):
    titles = Title.objects.all()
    return render(request, 'listings/listings_list.html',
                  {'titles': titles})


def listings_detail(request, id):
    title = Title.objects.get(id=id)
    return render(request, 'listings/listings_detail.html',
                  {'title': title})


def contact(request):
    return render(request, 'listings/contact.html')

