import requests

def search_gifs(search):
    url = 'https://api.giphy.com/v1/gifs/search'
    api = 'y4l4Smhjugdjw39hrBfgda1HrCVbSK98'

    params = {
        'api_key': api,
        'q': search,
        'limit': 5  # Ограничение на количество возвращаемых GIF
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        gif_urls = []

        for gif in data['data']:
            gif_urls.append(gif['url'])

        return gif_urls
        
    else:
        print('Error request in searching Gif! Pls try again!')
        return None


search_word = input("What gif you wanna search?: ")
gifs = search_gifs(search_word)

if gifs:
    print('Your GIFS: ')
    for gif in gifs:
        print(gif)

