This is a Flask API application for managing episodes and guest appearances on a late-night show. 
It uses PostgreSQL for database management, Flask-Migrate for handling database migrations, and Marshmallow for input validation.

The DB name is lateshow with below tables and their relations
             List of relations
 Schema |      Name       | Type  |  Owner  
--------+-----------------+-------+---------
 public | alembic_version | table | bernard
 public | appearances     | table | bernard
 public | episodes        | table | bernard
 public | guests          | table | bernard
(4 rows)

Database Models
Episode

    id: Integer, primary key.
    date: String, not nullable.
    number: Integer, not nullable.
    appearances: One-to-many relationship with the Appearance model.

Guest

    id: Integer, primary key.
    name: String, not nullable.
    occupation: String, not nullable.
    appearances: One-to-many relationship with the Appearance model.

Appearance

    id: Integer, primary key.
    rating: Integer, not nullable.
    episode_id: Foreign key to Episode.
    guest_id: Foreign key to Guest

To initialize the database, the below commands are followed
     flask db init
     flask db migrate -m "Initial migration."
     flask db upgrade