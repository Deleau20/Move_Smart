from flask import Flask, render_template, request, redirect, url_for
from models.incidents import Incident
from utils.database import initialize_db

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'your_database_name',
    'host': 'your_database_host',
    'port': 'your_database_port'
}

# Initialise la base de données
initialize_db(app)

@app.route('/')
def index():
    # Logique pour la page d'accueil
    return render_template('index.html')

@app.route('/incident', methods=['GET', 'POST'])
def incident():
    if request.method == 'POST':
        # Logique pour la soumission d'un incident
        title = request.form['title']
        description = request.form['description']
        location = request.form['location']
        user_id = request.form['user_id']

        incident = Incident(title=title, description=description, location=location, user_id=user_id)
        incident.save()

        return redirect(url_for('index'))

    # Logique pour afficher le formulaire de signalement d'incident
    return render_template('incident.html')

if __name__ == '_main_':
    app.run()