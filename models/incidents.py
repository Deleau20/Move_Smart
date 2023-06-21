from mongoengine import Document, StringField, ImageField, PointField


class Alerte(Document):
    
    prenom = StringField(required=True)
    nom = StringField(required=True)
    image = ImageField()
    localisation = StringField()
    titre = StringField(required=True)
    description = StringField(required=True)
