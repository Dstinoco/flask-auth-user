from flask import render_template, redirect, url_for, request, session
from app import app

@app.route('/')
def index():
    return "<h1>Teste aplicação</h1>"


@app.route("/teste")
def teste():
    return render_template('index.html'), 200


@app.route("/receber", methods=['GET', 'POST'])
def receber():
    if request.method == 'GET':
        return f"estou em receber <br> nome: {request.args.get('nome')}<br> idade: {request.args.get('idade')}", 200
    
    elif request.method == 'POST':
        return f"estou em receber <br> nome: {request.form['nome']}<br> idade: {request.form['idade']}", 200


@app.route("/session")
def login():
    return render_template("login.html")


@app.route('/validacao', methods=['POST'])
def validacao():
    if request.method == 'POST':
        session['login'] = request.form['login']
        session['password'] = request.form['password']
    return redirect(url_for('restrito'))
 

@app.route('/restrito')
def restrito():
    if "login" in session and 'password' in session and session['login'] == 'douglas' and session['password'] == 'teste':
        return f'Bem vindo {session["login"]}'
    else:
        return 'acesso negado'


@app.route("/sair")
def sair():
    session.pop('login', None)
    return redirect(url_for('login'))