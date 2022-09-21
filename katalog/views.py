from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    katalog_item = CatalogItem.objects.all()
    context = {
        "list_item" : katalog_item,
        "nama" : "Inez Bungaria Octaviana Pardede",
        "npm" : "2106751833"
    }
    return render(request, 'katalog.html', context) 
