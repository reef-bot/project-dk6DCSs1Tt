# backend/models.py

from app import db

class AtomBomb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(50), nullable=False)
    power_level = db.Column(db.String(50), nullable=False)

    def __init__(self, size, power_level):
        self.size = size
        self.power_level = power_level

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all_atom_bombs():
        return AtomBomb.query.all()

    @staticmethod
    def get_atom_bomb_by_id(atom_bomb_id):
        return AtomBomb.query.filter_by(id=atom_bomb_id).first()