from app import db
from flask_login import UserMixin

class Inventory(db.Model, UserMixin):
    """ Represents inventory table for database 'RestauranTech' """
    __tablename__ = 'inventory'
    quantity_in_stock = db.Column(db.Float, nullable=False)
    unit_of_measure = db.Column(db.String(16), nullable=False)
    average_price = db.Column(db.Float, nullable=False)
    shelf_life = db.Column(db.Integer, nullable=False)
    shelf_life_unit = db.Column(db.String(64), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)

    branch_id = db.Column(db.Integer, db.ForeignKey('branch.branch_id'), primary_key=True)
    asset_id = db.Column(db.Integer, db.ForeignKey('assets.asset_id'), primary_key=True)

    branch = db.relationship('Branch', back_populates='inventory')
    assets = db.relationship('Assets', back_populates='inventory')