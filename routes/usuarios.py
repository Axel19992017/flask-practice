from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash


from app import app, db, login_required

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        rows = db.execute("select * from usuario where username = :username", username = username)
        if len(rows) == 0:
            return render_template("usuarios/login.html", error="Usuario no existe")
        password_db = rows[0]["password"]
        if not check_password_hash(password_db, password):
            return render_template("usuarios/login.html", error="contraseña incorrecta")
        else:
            session["id_user"] = rows[0]["id"]
            return redirect("/")
    else:
        return render_template("usuarios/login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = generate_password_hash(request.form.get("password"))
        email = request.form.get("email")

        rows = db.execute("select * from usuario where username = :username", username = username)
        if len(rows) != 0:
            return render_template("usuarios/register.html", error="Usuario ya registrado")
        id_user = db.execute(f"INSERT INTO usuario (username,password, email) VALUES ('{username}','{password}', '{email}')")
        
        session["id_user"] = id_user
        return redirect("/")
    else:
        return render_template("usuarios/register.html")

@app.route("/listar-usuarios", methods=["GET"])
def mostrar_usuarios():

    filas = db.execute("SELECT * FROM usuario")
    return render_template("/usuarios/mostrar.html", filas = filas)
    


@app.route('/')
def index():
   return render_template("index.html")

@app.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect("/")