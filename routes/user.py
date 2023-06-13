from flask import Flask, render_template, request, Blueprint
from flask import jsonify, request
from models.user import Utilisateur

app = Flask(__name__)

route_utilisateur = Blueprint('user_router', __name__, url_prefix='/api/user')

@route_utilisateur.route('/', methods=['GET', 'POST'])
def accueil():
    return render_template('index.html')

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
        utilisateur = Utilisateur(prenom=prenom, nom=nom, email=email, mot_de_passe=mot_de_passe)
        print(utilisateur)
        utilisateur.save()      
        return render_template('accueil.html')
    except Exception as e:
        print(e)
        return e.__str__()
    
@route_utilisateur.route('/showconnect', methods=['GET'])
def showconnect():
    return render_template('connexion.html')
    
@route_utilisateur.route('/connexion', methods=['POST'])
def connexion():
    try:
        email = request.form['email']
        mot_de_passe = request.form['mot_de_passe']
        utilisateur = Utilisateur.objects(email=email, mot_de_passe=mot_de_passe).first()
        if utilisateur:
            return 'Connexion réussie !'
        else:
            return 'Email ou mot de passe incorrect !'
    except Exception as e:
        print(e)
        return e.__str__()

app.register_blueprint(route_utilisateur)

if __name__ == '__main__':
    app.run()
