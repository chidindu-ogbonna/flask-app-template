from werkzeug import security

from app import db
from flask_security import RoleMixin, SQLAlchemyUserDatastore, UserMixin

roles_users = db.Table('roles_users',
                       db.Column('user_id',
                                 db.Integer(), db.ForeignKey('users.id')),
                       db.Column('role_id',
                                 db.Integer(), db.ForeignKey('roles.id')))


class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return '<Role name={}>'.format(self.name)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24))
    password_hash = db.Column(db.String(124))
    email = db.Column(db.Text(), default=None, nullable=True)
    active = db.Column(db.Boolean(), default=None, nullable=True)
    roles = db.relationship(
        'Role',
        secondary=roles_users,
        backref=db.backref('users', lazy='dynamic'))

    # Uncomment the column if the SECURITY_CONFIRMABLE is set to True in config
    #  confirmed_at = db.Column(db.DateTime)

    # Uncomment the Columns if the SECURITY_TRACKABLE is set to True in config
    #  last_login_at = db.Column(db.DateTime)
    #  current_login_at = db.Column(db.DateTime)
    #  last_login_ip = db.Column(db.Integer)
    #  current_login_ip = db.Column(db.Integer)
    #  login_count = db.Column(db.Integer)

    def __repr__(self):
        return '<User user={}>'.format(self.username)

    @property
    def password(self):
        raise AttributeError('You cannot view this password')

    @password.setter
    def password(self, password):
        self.password_hash = security.generate_password_hash(password)

    # This is already provided by Flask-Security
    #  def verify_password(self, password):
    #      return security.check_password_hash(self.password_hash, password)


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
