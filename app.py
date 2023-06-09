from flask import Flask
from mongoengine import connect
from routes.user import route_utilisateur
from routes.alert import alerte_router
import certifi

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fredkesse1234'
connect(host="mongodb+srv://fredkesse1234:4f7E5YpybxrOqAlp@cluster0.qzxcffy.mongodb.net/", tlsCAFile=certifi.where())
# 4f7E5YpybxrOqAlp
# connect( db='Transport', username='user', password='9LTahJJoOYPUyn5T', host='mongodb://user:9LTahJJoOYPUyn5T@cluster2.0zjv9er.mongodb.net/transport')

app.register_blueprint(route_utilisateur, url_prefix='/')
app.register_blueprint(alerte_router, url_prefix='/')


    

if __name__ == '__main__':
    app.run(debug=True)


