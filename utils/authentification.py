from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User

def register_user(username, password):
    try:
        hashed_password = generate_password_hash(password)
        user = User(username=username, password=hashed_password)
        user.save()
    except Exception as e:
        raise Exception('Error registering user')

def login_user(username, password):
    try:
        user = User.objects(username=username).first()
        if user and check_password_hash(user.password, password):
            return user
        return None
    except Exception as e:
        raise Exception('Error logging in user')