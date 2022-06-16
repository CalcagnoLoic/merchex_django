from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Title


def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django!</h1>
        <p> Mes groupes préférés sont : </p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
            <li>{bands[3].name}</li>
            <li>{bands[4].name}</li>
        </ul>
        """)


def about(request):
    return HttpResponse('<h2>About Django!</h2> <p> Django c\'est marrant</p>')


def listing(request):
    titles = Title.objects.all()
    return HttpResponse(f"""
    <h1>Liste des annonces récentes : </h1>
    <ul>
        <li>{titles[0].name_title}</li>
        <li>{titles[1].name_title}</li>
        <li>{titles[2].name_title}</li>
        <li>{titles[3].name_title}</li>
    </ul>
    """)

def contact(request):
    return HttpResponse('<h1> test</h1>')
