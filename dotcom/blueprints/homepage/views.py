

from flask import current_app, g, redirect, render_template, request, session

from . import homepage_blueprint

import json
from bson import json_util

from test_lib.data.model.user import create_test_users, get_users
from test_lib.flask import force_scheme
from test_lib.flask.login import do_login

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
			request.form.get('username'), 
			request.form.get('password')
		)
		if not user:
			return json.dumps({'success': False})
		return json.dumps({'success': True})
	return render_template('login.html')


@homepage_blueprint.route('logout', methods=['GET'])
def logout():
	session.clear()
	return redirect('/')


@force_scheme('https')
#@login_required
@homepage_blueprint.route('users', methods=['GET'])
def list_users():
	filtered_by = request.args.get('city', None)
	ordered_by = request.args.get('gender', None)
	users = get_users(
		request.db,
		filtered_by,
		ordered_by
	)
	return render_template(
		'users.html',
		users=users
	)


@force_scheme('https')
#@login_required
@homepage_blueprint.route('files', methods=['GET'])
def list_files():
    return 'list files here'


#@login_required
@homepage_blueprint.route('statuses', methods=['GET'])
def statuses_handler():
    return 'statuses here'


