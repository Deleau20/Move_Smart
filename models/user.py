from mongoengine import Document, StringField

class Utilisateur(Document):
    prenom = StringField(required=True)
    nom = StringField(required=True)
    email = StringField(required=True)
    mot_de_passe = StringField(required=True)