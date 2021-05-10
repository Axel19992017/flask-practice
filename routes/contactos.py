from flask import render_template

from app import app, db, login_required

@app.route('/contactos')
@login_required
def contactos():
   return render_template("contactos/index.html")