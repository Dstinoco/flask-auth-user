from flask import render_template, redirect, url_for, request, session, flash
from projeto import app, bcrypt, database
from flask_login import login_required, login_user, logout_user, current_user
from projeto.forms import FormCriarConta, FormLogin
from projeto.models import Usuario






@app.route('/')
def index():
    return "<h1>Teste aplicação</h1>"


@app.route("/teste")
def teste():
    return render_template('index.html')


@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    formcadastro = FormCriarConta()
    
    if formcadastro.validate_on_submit():
        senha_hash = bcrypt.generate_password_hash(formcadastro.senha.data)
        
        novo_user = Usuario(
            email = formcadastro.email.data,
            username = formcadastro.username.data,
            senha = senha_hash
        )


        database.session.add(novo_user)
        database.session.commit()
        
        flash("Cadastro realizado com sucesso!', 'success'")
        return redirect("restrito")

    return render_template("cadastrar.html", form=formcadastro)



@app.route("/logar", methods=['GET', 'POST'])
def logar():
    if current_user.is_authenticated:
        return redirect(url_for("restrito"))
    
    form_login = FormLogin()
    
    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(username = form_login.username.data).first()
        
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario)
            flash("login realizado com sucesso!")
            return redirect(url_for("restrito"))
        else:
            flash('Login falhou. Verifique seu nome de usuário e senha.', 'danger')
    return render_template("logar.html", form=form_login)


@app.route("/receber", methods=['GET', 'POST'])
def receber():
    if request.method == 'GET':
        return f"estou em receber <br> nome: {request.args.get('nome')}<br> idade: {request.args.get('idade')}"
    
    elif request.method == 'POST':
        return f"estou em receber <br> nome: {request.form['nome']}<br> idade: {request.form['idade']}"


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
@login_required
def restrito():
    flash("login feito", 'danger')
    if "login" in session and 'password' in session and session['login'] == 'douglas' and session['password'] == 'teste':
        return f'Bem vindo {session["login"]}'
    else:
        return 'acesso negado'


@app.route("/sair")
def sair():
    logout_user()
    return redirect(url_for('logar'))