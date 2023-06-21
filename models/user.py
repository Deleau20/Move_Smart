from mongoengine import Document, StringField, ImageField, PointField

class Utilisateur(Document):
    prenom = StringField(required=True)
    nom = StringField(required=True)
    email = StringField(required=True, unique=True)
    mot_de_passe = StringField(required=True)