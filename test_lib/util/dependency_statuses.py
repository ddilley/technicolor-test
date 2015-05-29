
def mongo_available():
	from pymongo import MongoClient
	client = MongoClient('localhost', 27017)
	return (True, client.server_info()) if client.server_info() else (False, 'Mongo is down!')
	
def flask_available():
	try:
		from flask import current_app
		return(True, str(current_app._get_current_object()))
	except:
		return(False, 'Flask is down!')