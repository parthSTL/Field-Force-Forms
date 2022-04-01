import os

# Import Flask 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate    import Migrate

# Inject Flask magic
app = Flask(__name__)

# Load configuration
app.config.from_object('app.config.Config')

# Construct the DB Object (SQLAlchemy interface)
db = SQLAlchemy (app)