from flask import Flask, render_template, request, Blueprint, flash, redirect, url_for
from flask import jsonify, request
from models.user import Utilisateur
from passlib.hash import sha256_crypt
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fredkesse1234'

route_utilisateur = Blueprint('user_router', __name__, url_prefix='/api/user')


@route_utilisateur.route('/', methods=['GET', 'POST'])
def accueil():
    return render_template('index.html')


@route_utilisateur.route('/showlogin', methods=['GET'])
def showlogin():
    return render_template('inscription.html')


@route_utilisateur.route('/inscription', methods=['POST'])
def inscription():
    # sha256_crypt.verify()
    try:
        prenom = request.form['prenom']
        nom = request.form['nom']
        email = request.form['email']
        mot_de_passe = request.form['mot_de_passe']

        # Vérifier que le nom et le prénom ne contiennent pas de caractères spéciaux
        if not re.match(r'^[a-zA-Z\s]+$', prenom) or not re.match(r'^[a-zA-Z\s]+$', nom):
            flash('Le nom et le prénom ne doivent contenir que des lettres et des espaces.', 'warning')
            return redirect(url_for('user_router.showlogin'))
        
        # Vérifier que le mot de passe a une longueur supérieure à 8 caractères
        if len(mot_de_passe) <= 8:
            flash('Le mot de passe doit contenir plus de 8 caractères.', 'warning')
            return redirect(url_for('user_router.showlogin'))

        # Hacher le mot de passe
        mot_de_passe_hache = sha256_crypt.encrypt(mot_de_passe)

        utilisateur = Utilisateur(
            prenom=prenom, nom=nom, email=email, mot_de_passe=mot_de_passe_hache)
        utilisateur.save()

        return redirect(url_for('user_router.showconnect'))
    except Exception as e:
        return e.__str__()


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
            flash('Connexion réussie !', 'success')
            return render_template('accueil.html')
        else:
            flash('Email ou mot de passe incorrect !', 'danger')
            return redirect(url_for('user_router.showconnect'))

    except Exception as e:
        flash("Une erreur s'est produite lors de la connexion.', 'danger")
        return redirect(url_for('user_router.showconnect'))


app.register_blueprint(route_utilisateur)

if __name__ == '__main__':
    app.run()
