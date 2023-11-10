from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import render
from models import Game, GameDiscount, GameImage
import urllib.request
import json
import requests
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.serializers import PricingSerializer
# Create your views here.


@api_view(['GET'])
def get_price(request):
    game_discount = GameDiscount.objects.exclude(discount=0).order_by('id')
    discount_gameIDs = GameDiscount.objects.values_list('gameId', flat=True)
    game = Game.objects.filter(gameId__in=discount_gameIDs)
    game_image = GameImage.objects.filter(gameId__in=discount_gameIDs)
    Pricing = namedtuple('Pricing', ('game', 'game_discount', 'game_image'))
    pricing = Pricing(
        game=game,
        game_discount=game_discount,
        game_image=game_image
    )
    serializer = PricingSerializer(pricing)
    return Response(serializer.data)


