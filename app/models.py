from flask_security import UserMixin
#  from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug import security

from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(24))
    confirmed_at = db.Column(db.DateTime)
    password_hash = db.Column(db.String(124))
    last_login_at = db.Column(db.DateTime)
    current_login_at = db.Column(db.DateTime)
    last_login_ip = db.Column(db.Integer)
    current_login_ip = db.Column(db.Integer)
    login_count = db.Column(db.Integer)

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

#  @login_manager.user_loader
#  def load_user():
#      return User.query.get(int(user_id))
