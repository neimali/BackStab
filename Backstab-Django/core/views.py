from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import render
from models import Game, GameDiscount
import urllib.request
import json
import requests
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


# def get_game():
#     url = 'https://api.steampowered.com/ISteamApps/GetAppList/v2/'
#     r = requests.get(url)
#     data = r.json()
#     apps = data['applist']['apps']
#     for item in apps :
#         game = Game(gameId=item['appid'], gameName=item['name'])
#         game.save()
#
#
# def get_price(currency):
#     # url = 'http://store.steampowered.com/api/appdetails?appids=500&cc=us&filters=price_overview'
#     for game in Game.objects.values():
#         game_id = game['gameId']
#         payload = {'appids': game_id, 'cc': 'ca', 'filters': 'price_overview'}
#         r = requests.get('http://store.steampowered.com/api/appdetails', params=payload)
#         data = r.json()
#         data = data[str(game_id)]['data']['price_overview']
#         game_discount = GameDiscount(gameId=game_id, gameInitialPrice=data['initial'], gameFinalPrice=data['final'], currency=currency, discount=data['discount_percent'])
#         game_discount.save()

@api_view([])
def get_price(request):
    discount_game =GameDiscount.objects.exclude(discount=0).order_by('id')
    data ={'data':discount_game}
    return render(request, 'core/index.html', data)

