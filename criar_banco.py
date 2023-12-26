from projeto import app, database
from projeto.models import Usuario, Foto


with app.app_context():
    database.create_all()
