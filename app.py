from flask import Flask, request
from mongoengine import connect, Document, StringField
from models.user import Utilisateur

app = Flask(__name__)
connect('votre_base_de_donnees')

@app.route('/inscription', methods=['POST'])
def inscription():
    try:
        prenom = request.form['prenom']
        nom = request.form['nom']
        email = request.form['email']
        mot_de_passe = request.form['mot_de_passe']

        # Insérer les données dans la base de données
        utilisateur = Utilisateur(prenom=prenom, nom=nom, email=email, mot_de_passe=mot_de_passe)
        utilisateur.save()

        # Rediriger l'utilisateur vers une page de confirmation ou de succès
        return 'Inscription réussie !'

    except Exception as e:
        # Gérer l'erreur ici, par exemple, afficher un message d'erreur ou rediriger vers une page d'erreur
        return 'Une erreur s\'est produite lors de l\'inscription : ' + str(e)

if __name__ == '__main__':
    app.run()
