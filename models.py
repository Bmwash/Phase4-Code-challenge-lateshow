from flask_sqlalchemy import SQLAlchemy
from marshmallow import ValidationError

db = SQLAlchemy()

class Episode(db.Model):
    __tablename__ = 'episodes'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    appearances = db.relationship('Appearance', back_populates='episode', cascade="all, delete-orphan")

    def to_dict(self, include_appearances=True):
        episode_dict = {
            "id": self.id,
            "date": self.date,
            "number": self.number,
        }
        if include_appearances:
            episode_dict["appearances"] = [appearance.to_dict(include_episode=False) for appearance in self.appearances]
        return episode_dict

class Guest(db.Model):
    __tablename__ = 'guests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String, nullable=False)
    appearances = db.relationship('Appearance', back_populates='guest', cascade="all, delete-orphan")

    def to_dict(self, include_appearances=True):
        guest_dict = {
            "id": self.id,
            "name": self.name,
            "occupation": self.occupation
        }
        if include_appearances:
            guest_dict["appearances"] = [appearance.to_dict(include_guest=False) for appearance in self.appearances]
        return guest_dict

class Appearance(db.Model):
    __tablename__ = 'appearances'
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)

    episode = db.relationship('Episode', back_populates='appearances')
    guest = db.relationship('Guest', back_populates='appearances')

    def to_dict(self, include_episode=True, include_guest=True):
        appearance_dict = {
            "id": self.id,
            "rating": self.rating,
            "episode_id": self.episode_id,
            "guest_id": self.guest_id
        }
        if include_episode:
            appearance_dict["episode"] = {"id": self.episode.id, "number": self.episode.number}
        if include_guest:
            appearance_dict["guest"] = {"id": self.guest.id, "name": self.guest.name}
        return appearance_dict

    @staticmethod
    def validate_rating(value):
        if value < 1 or value > 5:
            raise ValidationError('Rating must be between 1 and 5.')
