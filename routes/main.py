from flask import render_template, redirect, url_for, flash, Flask
from models.user import User
from wtforms import RegistrationForm, LoginForm
from flask_login import LoginManager, login_user, current_user, logout_user

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    try:
        return User.objects(id=user_id).first()
    except Exception as e:
        flash('Error loading user', 'danger')
        return None


def create_app():
    try:
        # Création et configuration de l'application Flask
        app = Flask(__name__)
        app.config['SECRET_KEY'] = 'your_secret_key'

        login_manager.init_app(app)

        @app.route('/')
        def index():
            return render_template('index.html')

        @app.route('/register', methods=['GET', 'POST'])
        def register():
            try:
                form = RegistrationForm()
                if form.validate_on_submit():
                    user = User(username=form.username.data,
                                password=form.password.data)
                    user.save()
                    flash('Registration successful!', 'success')
                    return redirect(url_for('login'))
                return render_template('register.html', form=form)
            except Exception as e:
                flash('Erreur during registration', 'danger')
                return redirect(url_for('index'))

        @app.route('/login', methods=['GET', 'POST'])
        def login():
            try:
                form = LoginForm()
                if form.validate_on_submit():
                    user = User.objects(username=form.username.data).first()
                    if user and user.password == form.password.data:
                        login_user(user)
                        return redirect(url_for('index'))
                    else:
                        flash('Invalid username or password', 'danger')
                return render_template('login.html', form=form)
            except Exception as e:
                flash('Erreur during login', 'danger')
                return redirect(url_for('index'))

        @app.route('/logout')
        def logout():
            try:
                logout_user()
                return redirect(url_for('index'))
            except Exception as e:
                flash('Erreur logout', 'danger')
                return redirect(url_for('index'))

        return app

    except Exception as e:
        flash('Error creating app', 'danger')
        return None


if __name__ == '__main__':
    try:
        app = create_app()
        if app is not None:
            app.run()
    except Exception as e:
        print('An error occurred:', str(e))
