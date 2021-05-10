from flask import render_template

from app import app, db, login_required

@app.route('/biografia')
@login_required
def biografia():
   return render_template("biografia/index.html")