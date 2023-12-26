from app import app, database
from app.models import Usuario, Foto


with app.app_context():
    database.create_all()
