from flask import Flask, flash, redirect, render_template, request, session

from app import app, db, login_required

@app.route('/contactos')
@login_required
def contactos():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        numero = request.form.get("numero")
        correo = request.form.get("correo")
        
        db.execute(f"insert into contactos values(,,)")

    contactos = db.execute("select * from contactos where id_usuario =:Id", Id=session["id_user"])
    return render_template("contactos/index.html",contactos = contactos)