from flask import Flask, render_template, request, Blueprint, flash, redirect, url_for
from models.incidents import Alerte
from flask import Flask, render_template, request, Blueprint, flash, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fredkesse1234'


alerte_router = Blueprint('alerte_router', __name__, url_prefix='/api/alert')
route_utilisateur = Blueprint('user_router', __name__, url_prefix='/')


@alerte_router.route('/ajouter_alerte', methods=['POST'])
def ajouter_alerte():
    try:
        prenom = request.form['prenom']
        nom = request.form['nom']
        localisation = request.form.get('localisation')
        image = request.form.get('image')
        titre = request.form['titre']
        description = request.form['description']

        alerte = Alerte(
            prenom=prenom,
            nom=nom,
            localisation=localisation,
            image=image,
            titre=titre,
            description=description
        )
        alerte.save()
        flash('Alerte ajoutée avec succès !', 'success')
    except Exception as e:
        flash(f"Une erreur s'est produite lors de l'ajout de l'alerte. {e}", 'danger')
        print(e)

    return redirect(url_for('user_router.alertU'))


@alerte_router.route('/alert')
def liste_alertes():
    alertes = Alerte.objects()
    return render_template('incidents_user.html', alertes=alertes)


app.register_blueprint(alerte_router)
app.register_blueprint(route_utilisateur)


if __name__ == '__main__':
    app.run(debug=True)
