from app import app
from app.models import db, Pokemon, Item
from random import randint, choice


with app.app_context():


    pokemons = [
    {
        "number": 1,
        "imageUrl": '/images/pokemon_snaps/1.svg',
        "name": "Bulbasaur",
        "attack": 49,
        "defense": 49,
        "type": 'grass',
        "moves": [
          'tackle',
          'vine whip'
        ],
        "captured": True
      },
      {
        "number": 2,
        "imageUrl": '/images/pokemon_snaps/2.svg',
        "name": 'Ivysaur_1',
        "attack": 62,
        "defense": 63,
        "type": 'grass',
        "moves": [
          'tackle',
          'vine whip',
          'razor leaf'
        ],
        "captured": True
      },
      {
        "number": 3,
        "imageUrl": '/images/pokemon_snaps/3.svg',
        "name": 'Venusaur',
        "attack": 82,
        "defense": 83,
        "type": 'grass',
        "moves": [
          'tackle',
          'vine whip',
          'razor leaf'
        ],
        "captured": True
      },
      {
        "number": 4,
        "imageUrl": '/images/pokemon_snaps/4.svg',
        "name": 'Charmander',
        "attack": 52,
        "defense": 43,
        "type": 'fire',
        "moves": [
          'scratch',
          'ember',
          'metal claw'
        ],
        "captured": True
      },
      {
        "number": 5,
        "imageUrl": '/images/pokemon_snaps/5.svg',
        "name": 'Charmeleon_1',
        "attack": 64,
        "defense": 58,
        "type": 'fire',
        "moves": [
          'scratch',
          'ember',
          'metal claw',
          'flamethrower'
        ],
        "captured": True
      },
      {
        "number": 6,
        "imageUrl": '/images/pokemon_snaps/6.svg',
        "name": 'Charizard_2',
        "attack": 84,
        "defense": 78,
        "type": 'fire',
        "moves": [
          'flamethrower',
          'wing attack',
          'slash',
          'metal claw'
        ],
        "captured": True
      },
      {
        "number": 7,
        "imageUrl": '/images/pokemon_snaps/7.svg',
        "name": 'Squirtle',
        "attack": 48,
        "defense": 65,
        "type": 'water',
        "moves": [
          'tackle',
          'bubble',
          'water gun'
        ],
        "captured": True
      },
    {
        "number": 8,
        "imageUrl": '/images/pokemon_snaps/8.svg',
        "name": 'Wartortle',
        "attack": 63,
        "defense": 80,
        "type": 'water',
        "moves": [
          'tackle',
          'bubble',
          'water gun',
          'bite'
        ],
        "captured": True
      },
      {
        "number": 9,
        "imageUrl": '/images/pokemon_snaps/9.svg',
        "name": 'Blastoise',
        "attack": 83,
        "defense": 100,
        "type": 'water',
        "moves": [
          'hydro pump',
          'bubble',
          'water gun',
          'bite'
        ],
        "captured": True
      },
      {
        "number": 10,
        "imageUrl": '/images/pokemon_snaps/10.svg',
        "name": 'Caterpie',
        "attack": 30,
        "defense": 35,
        "type": 'bug',
        "moves": [
          'tackle'
        ],
        "captured": True
      },
      {
        "number": 12,
        "imageUrl": '/images/pokemon_snaps/12.svg',
        "name": 'Butterfree',
        "attack": 45,
        "defense": 50,
        "type": 'bug',
        "moves": [
          'confusion',
          'gust',
          'psybeam',
          'silver wind'
        ],
        "captured": True
      },
      {
        "number": 13,
        "imageUrl": '/images/pokemon_snaps/13.svg',
        "name": 'Weedle',
        "attack": 35,
        "defense": 30,
        "type": 'bug',
        "moves": [
          'poison sting'
        ],
        "captured": True
      },
      {
        "number": 16,
        "imageUrl": '/images/pokemon_snaps/16.svg',
        "name": 'Pidgey',
        "attack": 45,
        "defense": 40,
        "type": 'normal',
        "moves": [
          'tackle',
          'gust'
        ],
      },
      {
        "number": 17,
        "imageUrl": '/images/pokemon_snaps/17.svg',
        "name": 'Pidgeotto',
        "attack": 60,
        "defense": 55,
        "type": 'normal',
        "moves": [
          'tackle',
          'gust',
          'wing attack'
        ],
      },
      {
        "number": 18,
        "imageUrl": '/images/pokemon_snaps/18.svg',
        "name": 'Pidgeot',
        "attack": 80,
        "defense": 75,
        "type": 'normal',
        "moves": [
          'tackle',
          'gust',
          'wing attack'
        ],
      },
    ]


    images = [
        "/images/pokemon_berry.svg",
        "/images/pokemon_egg.svg",
        "/images/pokemon_potion.svg",
        "/images/pokemon_super_potion.svg",
        ]

    item_names = [
        "item 1",
        "item 2",
        "item 3",
    ]

    prices = randint(1, 100)
    happiness = randint(1, 100)

    # [db.session.add(Pokemon(**pokemon)) for pokemon in pokemons]
    # new_pokemon = Pokemon(number=1, imageUrl='/images/pokemon_snaps/1.svg', name="Bulbasaur", attack=49, defense=49, type='grass', moves='tackle, vine whip', captured=True)

    for pokemon in pokemons:
      pokemon['moves'] = ', '.join(pokemon['moves'])

    for pokemon in pokemons:
       db.session.add(Pokemon(**pokemon))


    for index in range(0,11):
        db.session.add(Item(name= choice(item_names), price= prices, happiness = happiness, imageUrl=choice(images)))

    db.session.commit()
    print('seeded')
