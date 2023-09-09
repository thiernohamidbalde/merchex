from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from listings.models import Band
from listings.models import Listing
from listings.forms import BandForm, ListingsForm, ContactUsForm

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

def band_create(request):
    if request.method =='POST':
        form = BandForm(request.POST)
        if form.is_valid():
            #creer une nouvelle band et la sauvegarder dans la bd
            band = form.save()
            #redirige vers la page de detail du groupe que nous venons de creer
            # nous pouvons fournir les arguments du motif url comme argument a la fonction de redirection
            return redirect('band-detail', band.id)
    else:
        form = BandForm()

    return render(request, 'listings/band_create.html',
                  {'form': form})

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

def listings_create(request):
    if request.method == 'POST':
        form = ListingsForm(request.POST)
        if form.is_valid():
            # creer une nouvelle annonce et la sauvegarder
            listing = form.save()
            # faire la redirection comme dans band
            return redirect('listing-detail', listing.id)
    else:
        form = ListingsForm()

    return render(request, 'listings/listings_create.html',
                  {'form': form})

def band_listing(request, band_listing_id):
    band_listing = Listing.objects.all()
    return render(request, 'listings/band_listing.html',
                  {'band_listing': band_listing})

def contact(request):
    if request.method == 'POST':
        # creer une instance de notre formulaire et le remplir avec les donees
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via Merchex'
                        f'Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent') # instruction de redirection si l'email est envoye
        # si le formulaire n'est pas valide, nous laissons l'execution continuer jusqu'au return
        # ci-dessous et afficher a nouveau le formulaire (avec des erreurs).
    else:
        # ceci doit etre une requete GET, donc creer un formulaire vide
        form = ContactUsForm() # ajout dun nouveau formulaire
    # return HttpResponse('<h1>Nous contacter</h1> <p>votre message</p>')
    return render(request, 'listings/contact.html',
                  {'form': form}) # passe ce formulaire de gabarit

def email_sent(request):
    return render(request, 'listings/email_sent.html')