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

# earned requests :
# https://giphy.com/gifs/disneystudios-the-lion-king-OqFpgF7bet1sRoCmpb
# https://giphy.com/gifs/uefa-sports-football-sport-JHjrh6oMG8ZfH1abnU
# https://giphy.com/gifs/ukraine-vj-loop-vjloops-3o85xz91Pwi4f4ncty
# https://giphy.com/gifs/evolution-axolotl-adapt-or-die-DDr9FUgtGgBKxBnF7T
