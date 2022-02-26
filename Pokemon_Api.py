import requests
import json

url_api = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    pokemon_name = input('Pokemon? >>> ').lower()
    pokemon_data_url = url_api + pokemon_name

    data = get_pokemon_data(pokemon_data_url)

    pokemon_type = [types['type']['name'] for types in data['types']]
    pokemon_abilities = [abilities['ability']['name'] for abilities in data['abilities']]

    print('---------------')
    print('name: ', (data['name']))
    print('types: ', pokemon_type)
    print('abilities: ', pokemon_abilities)
    print('height: ', data['height']/10,'m')
    print('weight: ', data['weight']/10,'kg')
    print('---------------')

    cont = input('Otro??? [Y/N] >>> ').lower()
    print('---------------')
    if cont == 'y':
        main()
    else:
        print('Good Bye!')

def get_pokemon_data(url_pokemon=''):

    pokemon_data = {
        'name': '',
        'height': '',
        'abilities': '',
        'types': '',
        'weight': ''
    }

    response = requests.get(url_pokemon)
    data = response.json()

    pokemon_data['name'] = data['name']
    pokemon_data['height'] = data['height']
    pokemon_data['abilities'] = data['abilities']
    pokemon_data['types'] = data['types']
    pokemon_data['weight'] = data['weight']

    return pokemon_data

if __name__ == '__main__':
    main()
