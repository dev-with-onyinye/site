from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Initialize extensions here
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
