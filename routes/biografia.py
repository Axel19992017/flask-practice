from flask import render_template

from app import app, db, login_required

@app.route("/biografia")
@login_required
def biografia():
   return render_template("biografia/index.html")

@app.route("/sumbit_biografia", methods=["POST"])
def submit_biografia():

    nombre_completo = request.form.get("nombre_completo")
    apodo = request.form.get("apodo")
    gustos_comida = request.form.get("gustos_comida")
    gustos_musica = request.form.get("gustos_musica")
    link_red_social = request.form.get("link_red_social")

    if not nombre_completo or not apodo or not gustos_comida or not gustos_musica or not link_red_social:
        flash("Datos incompletos")
        return redirect("/biografia"

    db.execute("""INSERT INTO biografia(user_id, nombre_completo, apodo, gustos_comida, gustos_musica, link_red_social)
    VALUES(:user_id, :nota)""", user_id=session["user_id"], nombre_completo = nombre_completo, apodo = apodo, gustos_comida = gustos_comida, link_red_social = link_red_social)
    return redirect("/biografia")

@app.route("/editar_biografia", methods=["POST"])
def editar_biografia():

    nombre_completo = request.form.get("nombre_completo")
    apodo = request.form.get("apodo")
    gustos_comida = request.form.get("gustos_comida")
    gustos_musica = request.form.get("gustos_musica")
    link_red_social = request.form.get("link_red_social")

    if not nombre_completo or not apodo or not gustos_comida or not gustos_musica or not link_red_social:
        flash("Datos incompletos para editar")
        return redirect("/biografia")

    db.execute("""UPDATE nombre_completo, apodo, gustos_comida, gustos_musica, link_red_social SET nombre_completo = :nombre, apodo = :apodo, gustos_musica = :musica, gustos_comida = :comida,link_red_social = :red_social where id= :id""",
               nombre = nombre_completo, apodo = :apodo, musica = gustos_musica, comida = gustos_comida, red_social = link_red_social, biografia_id = biografia_id)

    return redirect("/")
@app.route("/eliminar_biografia")


