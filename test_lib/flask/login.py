
from flask import g, request, session, current_app, flash, redirect, url_for
from functools import wraps
from hashlib import md5

from test_lib.util.security import is_logged_in, get_logged_in_user_id
from test_lib.data.model.user import get_user_by_id, get_user_by_username


def do_login(login, password):
    """
        Performs FICTITIOUS authentication
    """
    # call auth method
    user = get_user_by_username(request.db, login)
    if not user or not md5('%s'%password).hexdigest() == user.get('password_hash'):
        return None
    return user
    