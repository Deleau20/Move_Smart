from flask_mongoengine import MongoEngine

db = MongoEngine()

class User(db.Document):
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)

    def to_json(self):
        return {
            'id': str(self.id),
            'username': self.username
        }