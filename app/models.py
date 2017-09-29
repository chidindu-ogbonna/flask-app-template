from flask_login import UserMixin

from app import db, login_manager


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(24))

    def __repr__(self):
        return '<User user={}>'.format(self.user)


@login_manager.user_loader
def load_user():
    return User.query.get(int(user_id))
