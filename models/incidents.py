from mongoengine import Document, StringField, ImageField, PointField, FileField

class Alerte(Document):
    
    prenom = StringField(required=True)
    nom = StringField(required=True)
    image = FileField(required=True)
    localisation = StringField()
    titre = StringField(required=True)
    description = StringField(required=True)
