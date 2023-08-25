from flask import Blueprint
from ..models.items import Item

items = Blueprint('items', __name__)

@items.route('/<int:pokemonId>/items', methods=["GET"])
def home(pokemonId):
    items = Item.query.get(pokemonId).all()
    # print(item)
    for item in items:
        return item.dict_method()
