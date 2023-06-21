from flask import Flask, render_template, request, Blueprint, flash, redirect, url_for, session, jsonify
from models.user import Utilisateur
from passlib.hash import sha256_crypt
import re
from bson import ObjectId
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fredkesse1234'


def jsonify_with_objectid_support(data):
    def convert(obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        raise TypeError(
            f"Object of type {type(obj).__name__} is not JSON serializable")

    return json.dumps(data, default=convert)


def get_current_user():
    user_id = session.get('user_id')
    if user_id:
        # Remplacez cette ligne avec la méthode appropriée pour récupérer l'utilisateur
        utilisateur = Utilisateur.objects(id=user_id)
        return utilisateur[0]
    return None


route_utilisateur = Blueprint('user_router', __name__, url_prefix='/')


@route_utilisateur.route('/', methods=['GET', 'POST'])
def accueil():
    return render_template('index.html')


@route_utilisateur.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@route_utilisateur.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')


@route_utilisateur.route('/showlogin', methods=['GET'])
def showlogin():
    return render_template('inscription.html')


@route_utilisateur.route('/inscription', methods=['POST'])
def inscription():
    try:
        prenom = request.form['prenom']
        nom = request.form['nom']
        email = request.form['email']
        mot_de_passe = request.form['mot_de_passe']

        if not re.match(r'^[a-zA-Z\s]+$', prenom) or not re.match(r'^[a-zA-Z\s]+$', nom):
            flash(
                'Le nom et le prénom ne doivent contenir que des lettres et des espaces.', 'warning')
            return redirect(url_for('user_router.showlogin'))

        if len(mot_de_passe) <= 6:
            flash('Le mot de passe doit contenir plus de 6 caractères.', 'warning')
            return redirect(url_for('user_router.showlogin'))

        mot_de_passe_hache = sha256_crypt.encrypt(mot_de_passe)

        utilisateur = Utilisateur(
            prenom=prenom, nom=nom, email=email, mot_de_passe=mot_de_passe_hache)
        utilisateur.save()

        return redirect(url_for('user_router.showconnect'))
    except Exception as e:
        return str(e)


@route_utilisateur.route('/showconnect', methods=['GET'])
def showconnect():
    return render_template('connexion.html')


@route_utilisateur.route('/connexion', methods=['POST'])
def connexion():
    try:
        email = request.form['email']
        mot_de_passe = request.form['mot_de_passe']
        utilisateur = Utilisateur.objects(email=email).first()

        if utilisateur and sha256_crypt.verify(mot_de_passe, utilisateur.mot_de_passe):
            session['user_id'] = str(utilisateur["id"])
            flash('Connexion réussie !', 'success')
            return redirect(url_for('user_router.accueilU'))
        else:
            flash('Email ou mot de passe incorrect !', 'danger')
            return redirect(url_for('user_router.showconnect'))

    except Exception as e:
        flash("Une erreur s'est produite lors de la connexion.", 'danger')
        print(e)
        return redirect(url_for('user_router.showconnect'))


@route_utilisateur.route('/accueilU', methods=['GET'])
def accueilU():
    return render_template('accueil_user.html')


@route_utilisateur.route('/aboutU', methods=['GET'])
def aboutU():
    return render_template('about_user.html')


@route_utilisateur.route('/alertU', methods=['GET'])
def alertU():
    return render_template('alert_user.html')


@route_utilisateur.route('/incidentsU', methods=['GET'])
def incidentsU():
    return render_template('incidents_user.html')


@route_utilisateur.route('/contactU', methods=['GET'])
def contactU():
    return render_template('contact_user.html')


@route_utilisateur.route('/deconnexion', methods=['GET'])
def deconnexion():
    session.pop('user_id', None)
    flash('Vous avez été déconnecté.', 'success')
    return redirect(url_for('user_router.showconnect'))




app.register_blueprint(route_utilisateur)

if __name__ == '__main__':
    app.run(debug=True)