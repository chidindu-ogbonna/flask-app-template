from flask_login import UserMixin
from werkzeug import security

from app import db, login_manager


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(24))
    password_hash = db.Column(db.String(124))

    def __repr__(self):
        return '<User user={}>'.format(self.user)

    @property
    def password(self):
        raise AttributeError('You cannot view this password')

    @password.setter
    def password(self, password):
        self.password_hash = security.generate_password_hash(password)

    def verify_password(self, password):
        return security.check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user():
    return User.query.get(int(user_id))
