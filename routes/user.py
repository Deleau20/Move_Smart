from flask import Flask, render_template, request, Blueprint
from flask import jsonify, request
from models.user import Utilisateur

app = Flask(__name__)

route_utilisateur = Blueprint('user_router', __name__, url_prefix='/api/user')

@route_utilisateur.route('/')
def accueil():
    return render_template('index.html')

@route_utilisateur.route('/inscription', methods=['POST'])
def inscription():
    try:
        prenom = request.form['prenom']
        nom = request.form['nom']
        email = request.form['email']
        mot_de_passe = request.form['mot_de_passe']
        nouveau = Utilisateur(nom=nom, prenom=prenom, email=email, mot_de_passe=mot_de_passe)
        nouveau.save()       
        return 'Inscription réussie !'
    except Exception as e:
        return render_template()

app.register_blueprint(route_utilisateur)

if __name__ == '__main__':
    app.run()
