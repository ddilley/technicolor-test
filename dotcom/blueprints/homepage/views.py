

from flask import current_app, render_template, request, session

from . import homepage_blueprint
from test_lib.flask import force_scheme
# todo: login_required


@homepage_blueprint.route('/')
def homepage():
    return render_template('homepage.html')
    

@force_scheme('https')
@homepage_blueprint.route('login', methods=['GET', 'POST'])
def login():
    return 'login here'


@homepage_blueprint.route('logout', methods=['GET'])
def logout():
    return 'logout here'


@force_scheme('https')
#@login_required
@homepage_blueprint.route('users', methods=['GET'])
def list_users():
    return 'list users here'


@force_scheme('https')
#@login_required
@homepage_blueprint.route('files', methods=['GET'])
def list_files():
    return 'list files here'


#@login_required
@homepage_blueprint.route('statuses', methods=['GET'])
def statuses_handler():
    return 'statuses here'


