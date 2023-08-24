from .models import db

class Item(db.Model):
  __tablename__ = 'items'
  id = db.Column(db.Integer, primary_key=True)
  happiness = db.Column(db.Integer, nullable=False)
  imageUrl = db.Column(db.String(255), nullable=False)
  name = db.Column(db.String(255), nullable=False)
  price = db.Column(db.Integer, nullable=False)
  pokemonId = db.Column(db.Integer, db.ForeignKey('pokemons.id'))

  pokemon = db.relationship('Pokemon', back_populates='items')
