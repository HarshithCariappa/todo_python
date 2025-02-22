from flask import Flask
from config import Config
from models import db
from routes import TaskRoutes

# Initialize the Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db.init_app(app)
