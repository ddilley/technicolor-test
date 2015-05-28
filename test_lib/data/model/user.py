
from flask import request
from flask.ext.pymongo import PyMongo
from hashlib import md5


def create_user(db, user):
	"""
	Creates a user and returns it's unique ID
	"""
	users = db.users
	return users.insert(user)

def create_test_users(db):
	"""
	Creates test users in mongo DB
	"""
	db.users.remove()
	create_user(db,
		[{

			'username': 		'test',
			'password_hash':	md5('test').hexdigest(),
			'gender': 			1,
			'city': 			'Los Angeles'
		}]
	)
	create_user(db,
		[{
			'username': 		'Bob Barker',
			'password_hash':	md5('test').hexdigest(),
			'gender': 			1,
			'city': 			'Los Vegas'
		}]
	)
	create_user(db,
		[{
			'username': 		'Jane Doe',
			'password_hash':	md5('test').hexdigest(),
			'gender': 			0,
			'city': 			'Los Angeles'
		}]
	)
	create_user(db,
		[{
			'username': 		'Korra Avatar',
			'password_hash':	md5('test').hexdigest(),
			'gender': 			0,
			'city': 			'Los Los Angeles'
		}]
	)

def get_user_by_id(db, uid):
	user = db.users.find_one({'username': uid})
	return user[0] if len(user)>0 else None

def get_user_by_username(db, username):
	ret = db.users.find_one({'username': username})
	user = {}
	for key, value in ret.items():
		if key not in ['_id']:
			user['%s'%key] = value
	return user



	 
				
			
		
			
		
			
	
	