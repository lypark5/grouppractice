from .db import db


class Pokemon(db.Model):
  __tablename__ = 'pokemons'
  id = db.Column(db.Integer, primary_key=True)
  number = db.Column(db.Integer, nullable=False)
  attack = db.Column(db.Integer, nullable=False)
  defense = db.Column(db.Integer, nullable=False)
  imageUrl = db.Column(db.String, nullable=False)
  name = db.Column(db.String, nullable=False, unique=True)
  type = db.Column(db.String, nullable=False)
  moves = db.Column(db.String(255), nullable=False)
  encounterRate = db.Column(db.Float)
  catchRate = db.Column(db.Float)
  captured = db.Column(db.Boolean)

  items = db.relationship('Item', back_populates='pokemon')

  def dict_method(self):
    return {
        "id": self.id,
        "number": self.number,
        "attack": self.attack,
        "defense": self.defense,
        "imageUrl": self.imageUrl,
        "name": self.name,
        "type": self.type,
        "moves": self.moves,
        "encounterRate": self.encounterRate,
        "catchRate": self.catchRate,
        "captured": self.captured
    }
