from django.shortcuts import render
from example_1.models import footballplayer
from django.core.paginator import Paginator



# Create your views here.
def main(request):
    all_football_players = footballplayer.objects.all()

    
    context={
        "page_name":"Football players",
        "f_players": all_football_players,
    }
    return render(request, "example_1/main.html",context=context)