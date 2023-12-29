from sqlalchemy import text
from projeto import database, app
import pandas as pd

with app.app_context():
    conexao = database.engine.connect()
    consulta = text("SELECT * FROM usuario")
    resultados = conexao.execute(consulta)
