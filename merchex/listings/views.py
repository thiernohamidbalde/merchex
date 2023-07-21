
from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""<h1>Hello django</h1>
                         <p> mes groupes preferes sont : </p>
                         <ul>
                           <li>{bands[0].name}</li>
                           <li>{bands[1].name}</li>
                           <li>{bands[2].name}</li>
                         </ul>
""")

def about(request):
    return HttpResponse('<h1>A propos</h1> <p> nous adorons merchex</p>')

def listings(request):
    listing = Listing.objects.all()
    return HttpResponse(f"""<h1>Liste des sons</h1> <p> Vos titres sont : </p>
    <ul>
        <li>{listing[0].title}</li>
        <li>{listing[1].title}</li>
        <li>{listing[2].title}</li>
        <li>{listing[3].title}</li>
""")

def contact(request):
    return HttpResponse('<h1>Nous contacter</h1> <p>votre message</p>')