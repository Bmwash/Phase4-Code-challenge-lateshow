from flask import Blueprint, jsonify, request
from models import Episode, Guest, Appearance, db
from marshmallow import ValidationError

# Create a blueprint for the API
api = Blueprint('api', __name__)

# GET /episodes - Retrieve all episodes
@api.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes])

# GET /episodes/<id> - Retrieve a specific episode by ID
@api.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if episode is None:
        return jsonify({"error": "Episode not found"}), 404
    return jsonify(episode.to_dict())

# GET /guests - Retrieve all guests
@api.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests])

# POST /appearances - Create a new appearance
@api.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()

    # Validate rating
    try:
        Appearance.validate_rating(data['rating'])
    except ValidationError as ve:
        return jsonify({"errors": ve.messages}), 400

    # Create new appearance
    try:
        new_appearance = Appearance(
            rating=data['rating'],
            episode_id=data['episode_id'],
            guest_id=data['guest_id']
        )
        db.session.add(new_appearance)
        db.session.commit()
        return jsonify(new_appearance.to_dict()), 201
    except Exception as e:
        return jsonify({"errors": ["validation errors"]}), 400
