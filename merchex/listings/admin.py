from django.contrib import admin

#from bands.models import Band

# Register your models here.

from listings.models import Band, Listing

class BandAdmin(admin.ModelAdmin): # nous inserons lignes...
    list_display = ('name', 'year_formed', 'genre') # listes des champs que nous voulons sur l'affichage de la liste

class ListAdmin(admin.ModelAdmin):
    list_display = ('title', 'sold', 'year')


admin.site.register(Band, BandAdmin) # nous modifions cette ligne en ajoutant un 2e argument
admin.site.register(Listing, ListAdmin)