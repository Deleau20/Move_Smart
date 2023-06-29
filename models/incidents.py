from mongoengine import Document, StringField

class Alerte(Document):
    
    prenom = StringField(required=True)
    nom = StringField(required=True)
    localisation = StringField()
    titre = StringField(required=True)
    description = StringField(required=True)
