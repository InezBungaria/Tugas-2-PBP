from django.shortcuts import render
from mywatchlist.models import WatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    watchlist = WatchList.objects.all()
    message = ""
    watched = 0
    not_watched = 0

    for movie in watchlist:
        if movie.watched == True:
            watched += 1
        elif movie.watched == False:
            not_watched += 1
    if watched >= not_watched:
        message = "Selamat, kamu sudah banyak menonton!"
    elif not_watched >= watched:
        message = "Wah, kamu masih sedikit menonton!"



    context = {
        'watchlist' : watchlist,
        'nama' : 'Inez Bungaria Octaviana Pardede',
        'npm' : '2106751833',
        'message' : message
    }
    return render(request, "mywatchlist.html", context)

def show_xml (request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json (request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = WatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = WatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")