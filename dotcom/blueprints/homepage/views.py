

from flask import current_app, g, jsonify, render_template, request, session

from . import homepage_blueprint

from test_lib.data.model.user import create_test_users
from test_lib.flask import force_scheme
from test_lib.flask.login import login as do_login

# todo: login_required


@homepage_blueprint.route('/')
def homepage():
    return render_template('homepage.html')
    

@force_scheme('https')
@homepage_blueprint.route('login', methods=['GET', 'POST'])
def login():
	create_test_users(request.db)
	if request.method=='POST':
		user = do_login(
			request.args.get('username'), 
			request.args.get('password')
		)
		if not user:
			return jsonify({'success': False})
		return jsonify({'success': True, 'user': user})
	return render_template('login.html')


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


