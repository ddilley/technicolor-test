
from flask import g, request, session
# from test_lib.data.model.user import get_user_by_id

# logged in?
def is_logged_in():
    """
    Checks to see if the user is logged in
    """
    return 'usetId' in session


def get_logged_in_user_id():
    """
    Returns accountId in session if logged in or None
    """
    return session['userId'] if is_logged_in() else None


def get_logged_in_user(db):
    user_id = get_logged_in_user_id()
    if not user_id:
        return None
    #return get_user_by_id(db, user_id)
