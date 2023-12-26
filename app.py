from app import app
app.secret_key = 'MINHA_CHAVE01'




if __name__ == "__main__":
    app.run(debug=True)