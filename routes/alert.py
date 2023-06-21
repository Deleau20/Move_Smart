from flask import Flask, render_template, request, Blueprint, flash, redirect, url_for, session, jsonify
from models.incidents import Alerte
from passlib.hash import sha256_crypt
from flask import send_file
from mongoengine.fields import GridFSProxy
import re
from bson import ObjectId
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fredkesse1234'

alerte_router = Blueprint('alerte_router', __name__, url_prefix='/api/alert')
route_utilisateur = Blueprint('user_router', __name__, url_prefix='/')


@alerte_router.route('/ajouter_alerte', methods=['POST'])
def ajouter_alerte():
    try:
        prenom = request.form['prenom']
        nom = request.form['nom']
        image = request.files['image']
        localisation = request.form.get('localisation')
        titre = request.form['titre']
        description = request.form['description']

        alerte = Alerte(
            prenom=prenom,
            nom=nom,
            image=image,
            localisation=localisation,
            titre=titre,
            description=description
        )
        alerte.save()

        flash('Alerte ajoutée avec succès !', 'success')
    except Exception as e:

        flash(f"Une erreur s'est produite lors de l'ajout de l'alerte. {e}", 'danger')
        print(e)

    return redirect(url_for('user_router.alertU'))



@alerte_router.route('/image/<id>')
def image(id):
    fs = GridFSProxy(Alerte._get_db())
    alerte = Alerte.objects.get(id=id)
    if alerte.image:
        grid_out = fs.get(alerte.image.grid_id)
        if grid_out:
            response = send_file(grid_out, mimetype=grid_out.content_type)
            response.headers['Cache-Control'] = 'no-store'  # Pour éviter la mise en cache de l'image
            return response

    # Image par défaut ou réponse 404 si aucune image n'est trouvée
    return send_file('path/vers/une/image/par/defaut.jpg')



@alerte_router.route('/alert')
def liste_alertes():
    alertes = Alerte.objects()
    return render_template('incidents_user.html', alertes=alertes)