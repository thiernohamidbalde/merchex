
from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html',
                  context={'bands': bands})

def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request, 'listings/band_detail.html',
                  {'band': band})
   # return HttpResponse(f"""<h1>Hello django</h1>
    #                     <p> mes groupes preferes sont : </p>
     #                    <ul>
       #                    <li>{bands[0].name}</li>
        #                   <li>{bands[1].name}</li>
        #                   <li>{bands[2].name}</li>
         #                </ul>
#""")

def about(request):
    #return HttpResponse('<h1>A propos</h1> <p> nous adorons merchex</p>')
    return render(request, 'listings/about.html')

def listings(request):
    listing = Listing.objects.all()
    return render(request, 'listings/listings.html',
                  context={'listing': listing})

def listing_detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    return render(request, 'listings/listing_detail.html',
                  {'listing': listing})

def contact(request):
    #return HttpResponse('<h1>Nous contacter</h1> <p>votre message</p>')
    return render(request, 'listings/contact.html')