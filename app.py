from flask import Flask
from extensions import db, bcrypt, login_manager  # Import from extensions.py
from models import User, DreamEntry  # Now safely import models after db initialization

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# Initialize the app with db, bcrypt, and login_manager
db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)

# User loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    app.run(debug=True)
