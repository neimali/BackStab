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
    for game in Game.objects.values():
        game_id = game['gameId']
        payload = {'appids': game_id, 'cc': 'ca', 'filters': 'price_overview'}
        r = requests.get('http://store.steampowered.com/api/appdetails', params=payload)
        data = r.json()
        try:
            data = data[str(game_id)]['data']['price_overview']
            game_discount = GameDiscount(gameId=game_id, gameInitialPrice=data['initial'], gameFinalPrice=data['final'], currency='ca', discount=data['discount_percent'])
            game_discount.save()
        except:
            continue
        