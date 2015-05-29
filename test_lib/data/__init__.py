
from flask import request
from flask.ext.pymongo import PyMongo
from pymongo import MongoClient

"""
    This registers mongo as the apps DB
"""

def register_db_session(app, use_manipulator=True):
    """
    Creates the db session
    """

    @app.before_request
    def open_db_session():
        client = MongoClient('localhost', 27017)
        db = client['test']
        request.db = db

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
