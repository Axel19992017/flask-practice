from flask import render_template

from app import app, db, login_required

@app.route('/mensajes')
@login_required
def mensajes():
    mensaje = db.execute("SELECT id_remitente, id_emisor, contenido, fecha FROM mensajes WHERE id=:id_",
                            id_=session['id_user'])

    return render_template("mensajes/index.html", mensaje=mensaje)



