from flask import render_template, flash

from app import app, db, login_required

@app.route('/anotaciones')
@login_required
def anotaciones():

    consulta = db.execute("SELECT * FROM  anotaciones WHERE id_usuario = :id ",
                            id = session["id_user"])
    return render_template("anotaciones/index.html", anotaciones=consulta)

@app.route('/agregar')
def agregar():
    if request.method == "POST"
        titulo = request.form.get("titulo")
        contenido = request.form.get("contenido")

        if not request.form.get("titulo"):
            return apology("invalid title",403)

        if not request.form.get("contenido"):
            return apology("invalid content")

        rows = db.execute("INSERT INTO anotaciones (id_usuario, titulo, contenido) VALUES (:id_usuario, :titulo, :contenido)",
                            id_usuario = session["id_user"], titulo = titulo, contenido = contenido)
        return redirect("/anotaciones")

@app.route('/actualizar')
def actualizar():

    if request.method == "POST"

        id = request.form.get("id")
        titulo = request.form.get("titulo")
        contenido = request.form.get("contenido")

        if not request.form.get("id"):
            return apology("invalid id",403)

        if not request.form.get("titulo"):
            return apology("invalid title",403)

        if not request.form.get("contenido"):
            return apology("invalid content")

        rows = db.execute("UPDATE anotaciones SET titulo = :titulo, contenido = :contenido WHERE id = :id",
                            titulo = titulo, contenido = contenido, id = id)
        return redirect("/anotaciones")

@app.route('/eliminar')
def eliminar():

    if request.method == "POST"

        id = request.form.get("id")

        if not request.form.get("id"):
            return apology("invalid id",403)

        rows = db.execute("DELETE FROM anotaciones WHERE id = :id",
                            id = id)
        return redirect("/anotaciones")



def apology(message, code=400):
    """Renders message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("anotaciones/apology.html", top=code, bottom=escape(message))


