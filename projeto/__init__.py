from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import secrets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///comunidade.db"

if "SECRET_KEY" not in app.config:
    app.config['SECRET_KEY'] = secrets.token_hex(16)

database = SQLAlchemy(app)
bcrypt =  Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'



from projeto import routes