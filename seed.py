from app import app, db
from models import Episode, Guest, Appearance

episodes_data = [
    {'date': '2024-01-01', 'number': 1},
    {'date': '2024-01-08', 'number': 2},
    {'date': '2024-01-15', 'number': 3},
]

guests_data = [
    {'name': 'Omosh', 'occupation': 'Actor'},
    {'name': 'Crazy Kernnar', 'occupation': 'Comedian'},
    {'name': 'Stevo SimpleBoy', 'occupation': 'Musician'},
]

appearances_data = [
    {'rating': 5, 'episode_number': 1, 'guest_name': 'Crazy Kennar'},
    {'rating': 4, 'episode_number': 2, 'guest_name': 'Stevo SimpleBoy'},
    {'rating': 3, 'episode_number': 3, 'guest_name': 'Omosh'},
]

def seed_data():
    with app.app_context():
   
        db.create_all()

    
        Episode.query.delete()
        Guest.query.delete()
        Appearance.query.delete()

  
        for episode in episodes_data:
            new_episode = Episode(date=episode['date'], number=episode['number'])
            db.session.add(new_episode)

  
        for guest in guests_data:
            new_guest = Guest(name=guest['name'], occupation=guest['occupation'])
            db.session.add(new_guest)

        for appearance in appearances_data:
            episode = Episode.query.filter_by(number=appearance['episode_number']).first()
            guest = Guest.query.filter_by(name=appearance['guest_name']).first()
            if episode and guest:
                new_appearance = Appearance(rating=appearance['rating'], episode_id=episode.id, guest_id=guest.id)
                db.session.add(new_appearance)

        db.session.commit()
        print("Database seeded successfully.")

if __name__ == '__main__':
    seed_data()
