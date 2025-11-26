from flask import Flask, render_template, request
from olympics import db

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    """Page d'accueil simple."""
    return "<h1>Interface Web Olympics</h1><p>Utilisez /discipline/&lt;id&gt; pour afficher un classement.</p>"


@app.route("/discipline/<int:discipline_id>")
def top_discipline(discipline_id):
    """
    Affiche le top des pays pour une discipline donnée.
    Exemple :
        /discipline/3?top=5
    """
    top = request.args.get("top", default=5, type=int)

    # Appel à la fonction DB existante
    rows = db.get_top_countries_by_discipline(discipline_id, top)

    return render_template("top_discipline.html",
                           discipline_id=discipline_id,
                           top=top,
                           rows=rows)
