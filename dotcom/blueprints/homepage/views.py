

from flask import current_app, g, redirect, render_template, request, session

from . import homepage_blueprint

import json
from bson import json_util

from test_lib.data.model.user import create_test_users, get_users
from test_lib.flask import force_scheme
from test_lib.flask.login import do_login
from test_lib.util.files import list_dirs_files

import os

# relative to this file(!)
PROJECT_ROOT = os.path.abspath(os.path.abspath(__file__)+'../../../../../')


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
@homepage_blueprint.route('users', methods=['GET'])
def list_users():
	city = request.args.get('city', None)
	ordered_by = request.args.get('ordered_by', None)
	users = get_users(request.db, city, '%s'%ordered_by)
	return render_template(
		'users.html',
		users=users,
		city=city,
		ordered_by=ordered_by
	)


@force_scheme('https')
@homepage_blueprint.route('files', methods=['GET', 'POST'])
def list_files():
	path = str(request.form.get('path', '')) if request.method=='POST' \
	else str(request.args.get('path', ''))
	if path:
		if not path[0]=='/':
			path = '/%s'%path
		files = list_dirs_files(path, PROJECT_ROOT)
		if not files:
			if request.method=='POST':
				return json.dumps({'success':True, 'ret': 'No such folder or empty'})
				files = []
		if request.method=='POST':
			return json.dumps({'success':True, 'ret':files})
	return render_template(
		'list_files.html',
		ret=files if path and files else None,
		file_scope=PROJECT_ROOT
	)


@homepage_blueprint.route('statuses', methods=['GET'])
def statuses_handler():
    return 'statuses here'


