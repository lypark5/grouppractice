from flask import Blueprint, request, redirect
from ..models.db import db
from ..models.pokemon import Pokemon
from ..models.pokemon_type import types
from ..forms.forms import CreatePokemon

pokemon = Blueprint('pokemon', __name__)

@pokemon.route("")
def home():
    print('home route')
    all_pokemons = Pokemon.query.all()
    pokemons = [pokemon.dict_method() for pokemon in all_pokemons]
    print(all_pokemons)
    return pokemons

@pokemon.route('/<int:id>')
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
    print('types route')
    # return {"types": types}
    return types

@pokemon.route("", methods=["POST"])
def create_pokemon():
    form = CreatePokemon()
    form['csrf_token'].data = request.cookies['csrf_token']
    # print('Form Data brackets...', form.data['move1'])
    # print('Form Data...', form.data['move2'])
    print('MOVES COMBINED...', str(form.data["move1"]) + ", " + str(form.data["move2"]))

    if form.validate_on_submit():
        data = form.data
        # moves = str(data["move1"] + ", " + data["move2"])
        new_pokemon = Pokemon(
            number=data["number"],
            attack=data["attack"],
            defense=data['defense'],
            imageUrl=data['imageUrl'],
            name=data['name'],
            moves=str(data['moves']),
            type=data['type']
            )
        db.session.add(new_pokemon)
        db.session.commit()

    if form.errors:
        print(form.errors)
        # return form.errors
