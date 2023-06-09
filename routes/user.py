from flask import Flask, render_template, request, Blueprint
from flask import jsonify, request
from models.user import Utilisateur

route_utilisateur = Blueprint('user_router', __name__, url_prefix='/api/user')

@route_utilisateur.route('/', methods=['GET', 'POST'])
def accueil():
    return render_template('index.html')

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
        return 'Inscription réussie !'
    except Exception as e:
        return e.__str__()

# app.register_blueprint(route_utilisateur)

# if __name__ == '__main__':
#     app.run()
