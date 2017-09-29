from flask import Blueprint, render_template, url_for, redirect
from ..forms import RegistrationForm, LoginForm
# uncomment this to start working with the models
#  from ..models import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        redirect(url_for('main.index'))
    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        redirect(url_for('auth.login'))
    return render_template('auth/register.html')
