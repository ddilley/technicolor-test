

from flask import current_app, render_template, request, session

from . import homepage_blueprint
from test_lib.flask import force_scheme
# todo: login_required


@homepage_blueprint.route('/')
def homepage():
    return render_template('homepage.html')
    

@homepage_blueprint.route('login', methods=['GET', 'POST'])
@force_scheme('https')
def login():
    return 'login here'


@homepage_blueprint.route('logout')
def logout():
    return 'logout here'


@homepage_blueprint.route('users')
@force_scheme('https')
#@login_required
def list_users():
    return 'list users here'


@homepage_blueprint.route('files')
@force_scheme('https')
#@login_required
def list_files():
    return 'list files here'


@homepage_blueprint.route('statuses')
#@login_required
def statuses_handler():
    return 'statuses here'


