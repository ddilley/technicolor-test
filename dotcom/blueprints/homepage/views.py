

from flask import current_app, g, redirect, render_template, request, session

from . import homepage_blueprint

import json
from bson import json_util

from test_lib.data.model.user import create_test_users, get_users
from test_lib.flask import force_scheme
from test_lib.flask.login import do_login
from test_lib.util.files import list_dirs_files


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
	folder_name = request.form.get('folder_name', '')
	folder_name = '%s'%folder_name
	files = list_dirs_files(folder_name)
	if files:
		ret = str(list_dirs_files(folder_name))
	if request.method=='POST':
		if not files:
			return json.dumps({'success':True, 'ret': 'No such folder or empty'})
		return json.dumps({'success':True, 'ret':ret})
	return render_template('list_files.html', ret=ret if files else None)


@homepage_blueprint.route('statuses', methods=['GET'])
def statuses_handler():
    return 'statuses here'


