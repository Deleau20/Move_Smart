from flask import Flask, render_template, request, Blueprint, flash, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from models.incidents import Alerte
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fredkesse1234'
app.config['UPLOAD_FOLDER'] = './image'  # Nouveau dossier de destination pour les images téléchargées
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}  # Extensions de fichiers autorisées

alerte_router = Blueprint('alerte_router', __name__, url_prefix='/api/alert')
route_utilisateur = Blueprint('user_router', __name__, url_prefix='/')


def allowed_file(filename):
    # Vérifie si l'extension du fichier est autorisée
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@alerte_router.route('/ajouter_alerte', methods=['POST'])
def ajouter_alerte():
    try:
        prenom = request.form['prenom']
        nom = request.form['nom']
        image = request.files['image']
        filename = image.filename
        localisation = request.form.get('localisation')
        titre = request.form['titre']
        description = request.form['description']

        if image and allowed_file(image.filename):
            # Génère un nom de fichier sécurisé
            filename = secure_filename(image.filename)
            print(filename)
            # Enregistre l'image dans le dossier UPLOAD_FOLDER en spécifiant l'encodage
            image.stream.seek(0)  # Réinitialise la position de lecture du flux
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename), buffer_size=16384)



        else:
            flash("Format de fichier d'image non autorisé", 'danger')
            return redirect(url_for('user_router.alertU'))

        alerte = Alerte(
            prenom=prenom,
            nom=nom,
            image=filename,  # Assigner le nom de fichier à la propriété "image" du modèle
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


@route_utilisateur.route('/image/<filename>')
def uploaded_file(filename):
    # Renvoie le fichier image téléchargé
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


app.register_blueprint(alerte_router)
app.register_blueprint(route_utilisateur)


if __name__ == '__main__':
    app.run(debug=True)
