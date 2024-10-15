from flask import Flask
from models import db
from routes import api
from flask_migrate import Migrate

# Initialize the Flask application
app = Flask(__name__)

# Configure the PostgreSQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bernard:slack2024@localhost/lateshow'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration functionality
db.init_app(app)
migrate = Migrate(app, db)

# Register the routes/blueprints
app.register_blueprint(api, url_prefix='/api')

# Create the database tables (if they don't already exist)
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Creates tables as per the models, if they don't already exist
    # Start the application
    app.run(debug=True)
