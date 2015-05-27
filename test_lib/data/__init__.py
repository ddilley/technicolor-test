
from flask import request
from flask.ext.pymongo import PyMongo

def register_db_session(app):
    """
    Creates the db session
    """
    mongo = PyMongo(app)
    
    @app.before_request
    def open_db_session():
        request.db = mongo.db
        # load test data into mongodb for authentication
        # routed at homepage.login
        

    @app.after_request
    def commit_db_session(response):
        if hasattr(request, 'db') and request.db is not None:
            #request.db.commit()
            pass
        return response

    @app.teardown_request
    def close_db_session(error=False):
        if hasattr(request, 'db') and request.db is not None:
            request.db.logout()
            del(request.db)

    @app.errorhandler(500)
    def handle_error(e):
        if hasattr(request, 'db') and request.db is not None:
            pass
            #request.db.rollback()
