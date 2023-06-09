# from datetime import datetime
# from flask_mongoengine import MongoEngine

# db = MongoEngine()

# class Incident(db.Document):
#     title = db.StringField(required=True)
#     description = db.StringField(required=True)
#     location = db.StringField(required=True)
#     timestamp = db.DateTimeField(default=datetime.now, required=True)
#     user_id = db.ObjectIdField(required=True)

#     def to_json(self):
#         return {
#             'id': str(self.id),
#             'title': self.title,
#             'description': self.description,
#             'location': self.location,
#             'timestamp': self.timestamp.isoformat(),
#             'user_id': str(self.user_id)
#         }