from flask import Blueprint, request, redirect
from ..models.db import db
from ..models.pokemon import Pokemon
from ..models.items import Item
from ..models.pokemon_type import types
from ..forms.forms import CreatePokemon, CreateItem
from random import choice
pokemon = Blueprint('pokemon', __name__)

images = [
        "/images/pokemon_berry.svg",
        "/images/pokemon_egg.svg",
        "/images/pokemon_potion.svg",
        "/images/pokemon_super_potion.svg",
        ]

@pokemon.route('/<int:pokemonId>/items', methods=['GET'])
def get_item(pokemonId):
    items = Item.query.filter(Item.pokemonId == pokemonId).all()
    
    return [item.dict_method() for item in items]
    

@pokemon.route('/<int:pokemonId>/items', methods=['POST'])
def create_item(pokemonId):
    form = CreateItem()
    pokemon = Pokemon.query.get(pokemonId)
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = form.data
        new_item = Item(
            name = data['name'],
            happiness = data['happiness'],
            price = data['price'],
            imageUrl = choice(images)
        )
        new_item.pokemon = pokemon
        db.session.add(new_item)
        db.session.commit()
        print(pokemon.items)
        return new_item.dict_method() 
    elif form.errors:
        return { 'errors' :form.errors}

    

@pokemon.route("")
def home():
    all_pokemons = Pokemon.query.all()
        
    pokemons = [pokemon.dict_method() for pokemon in all_pokemons]
    for pokemon in pokemons:
        pokemon['moves'] = [item for item in pokemon['moves'].split(',')]
    return pokemons

@pokemon.route('/<int:id>', methods=['PUT'])
def edit_pokemon(id):
    form = CreatePokemon()
    edit_pokemon = Pokemon.query.get(id)
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        data = form.data
        edit_pokemon.number = data['number']
        edit_pokemon.attack = data['attack']
        edit_pokemon.defense = data['defense']
        edit_pokemon.imageUrl = data['imageUrl']
        edit_pokemon.name = data['name']
        edit_pokemon.type = data['type']
        edit_pokemon.moves = str(data["move1"] + ", " + data["move2"])
        db.session.commit()
        edit_pokemon = edit_pokemon.dict_method()
        edit_pokemon['moves'] = [item for item in edit_pokemon['moves'].split(',')]
        return edit_pokemon


    elif form.errors:
        return { 'errors': form.errors }


    

@pokemon.route('/<int:id>', methods=['GET'])
def single_pokemon(id):
    one_pokemon = Pokemon.query.get(id)
    # print('ONE POKEMON...', one_pokemon)
    new_moves = []
    moves_list = one_pokemon.moves.split(', ')
    for move in moves_list:
       new_moves.append(move)

    one_pokemon.moves = new_moves

    # print('MOVES....', one_pokemon.moves)
    return one_pokemon.dict_method()

@pokemon.route("/types")
def get_types():
    # return {"types": types}
    return types

@pokemon.route("", methods=["POST"])
def create_pokemon():
    form = CreatePokemon()
    form['csrf_token'].data = request.cookies['csrf_token']
    # print('Form Data brackets...', form.data['move1'])
    # print('Form Data...', form.data['move2'])
    
    if form.validate_on_submit():
        data = form.data
        moves = str(data["move1"] + ", " + data["move2"])
        new_pokemon = Pokemon(
            number=data["number"],
            attack=data["attack"],
            defense=data['defense'],
            imageUrl=data['imageUrl'],
            name=data['name'],
            moves=moves,
            type=data['type']
            )
        db.session.add(new_pokemon)
        db.session.commit()
        new_pokemon = new_pokemon.dict_method()
        new_pokemon['moves'] = [data["move1"],data["move2"]]
        return new_pokemon

    if form.errors:
        print(form.errors)
        # return form.errors
