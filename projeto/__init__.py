from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import secrets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///comunidade.db"


app.config['SECRET_KEY'] = '5d47052b3a8493d24f700710c81df5fe'


database = SQLAlchemy(app)
bcrypt =  Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'



from projeto import routes