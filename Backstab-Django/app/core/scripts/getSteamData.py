from core.models import Game, GameDiscount  
import requests

def run():
    get_game()
    get_price()


def get_game():
    url = 'https://api.steampowered.com/ISteamApps/GetAppList/v2/'
    r = requests.get(url)
    data = r.json()
    apps = data['applist']['apps']
    for item in apps :
        game = Game(gameId=item['appid'], gameName=item['name'])
        game.save()


def get_price():
    # url = 'http://store.steampowered.com/api/appdetails?appids=500&cc=us&filters=price_overview'
    game_ids = Game.objects.values_list('gameId', flat=True)
    game_ids = game_ids[:50]
    query_str = ','.join(map(str, game_ids))
    payload = {'appids': query_str, 'cc': 'ca', 'filters': 'price_overview'}
    r = requests.get('http://store.steampowered.com/api/appdetails', params=payload)
    data = r.json()
    for game_id in data.keys():
        if data[game_id]['success']:
            try:
                price_detail = data[game_id]['data']['price_overview']
                game_discount = GameDiscount(gameId=game_id, gameInitialPrice=price_detail['initial'],
                                             gameFinalPrice=price_detail['final'], currency='ca',
                                             discount=price_detail['discount_percent'])
                game_discount.save()
            except:
                continue
        else:
            continue
