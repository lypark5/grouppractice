from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, DateField, SelectField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange
from ..models.pokemon_type import types


class CreatePokemon(FlaskForm):
  number = IntegerField('Number', validators=[DataRequired(), NumberRange(min=1)])
  attack = IntegerField('Attack', validators=[DataRequired(), NumberRange(min=0, max=100)])
  defense = IntegerField('Defense', validators=[DataRequired(), NumberRange(min=0, max=100)])
  imageUrl = StringField('Image URL', validators=[DataRequired()])
  name = StringField('Name', validators=[DataRequired()])
  move1 = StringField('Move 1', validators=[DataRequired()])
  move2 = StringField('Move 2', validators=[DataRequired()])
  type = SelectField('Type', choices=[types])
  submit = SubmitField('CREATE NEW POKEMON')

class CreateItem(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])
  happiness = IntegerField('Happiness', validators=[DataRequired(), NumberRange(min=0, max=100)])
  price = IntegerField('Price', validators=[DataRequired()])
  submit = SubmitField('ADD ITEM')
