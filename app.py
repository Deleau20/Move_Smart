from flask import Flask
from mongoengine import connect
from routes.user import route_utilisateur

app = Flask(__name__)
# connect("mongodb+srv://fredkesse1234:9LTahJJoOYPUyn5T@cluster2.0zjv9er.mongodb.net")
connect( db='Transport', username='user', password='9LTahJJoOYPUyn5T', host='mongodb://user:9LTahJJoOYPUyn5T@cluster2.0zjv9er.mongodb.net/transport')

app.register_blueprint(route_utilisateur, url_prefix='/api/user')


    

if __name__ == '__main__':
    app.run(debug=True)


