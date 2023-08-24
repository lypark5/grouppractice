from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, DateField, SelectField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length
from ..models import types


class CreatePokemon(FlaskForm):
  number = IntegerField('Number', [DataRequired()])
  attack = IntegerField('Attack', [DataRequired()])
  defense = IntegerField('Defense', [DataRequired()])
  imageUrl = StringField('Image URL', [DataRequired()])
  name = StringField('Name', [DataRequired()])
  move1 = StringField('Move 1', [DataRequired()])
  move2 = StringField('Move 2', [DataRequired()])
  type = SelectField('Type', choices=types)
  submit = SubmitField('CREATE NEW POKEMON')

class CreateItem(FlaskForm):
  name = StringField('Name', [DataRequired()])
  happiness = IntegerField('Happiness', [DataRequired()])
  price = IntegerField('Price', [DataRequired()])
  submit = SubmitField('ADD ITEM')
