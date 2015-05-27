
from flask import g, request, session, current_app, flash, redirect, url_for
from functools import wraps
from hashlib import md5

from test_lib.util.security import is_logged_in, get_logged_in_user_id
from test_lib.data.model.user import get_user_by_id, get_user_by_username


def login_required(fn):
    """
    Login required decorator
    """
    @wraps(fn)
    def decorated_view(*args, **kwargs):
        if not is_logged_in():
            return current_app.login_manager.unauthorized()
        return fn(*args, **kwargs)
    return decorated_view


def login(login, password):
    """
    Authenticates and logs in a user, None is returned
    if the authentication failed
    """
    return current_app.auth_mgr.login(login, password)


def login_user(user):
    """
    Logs in the given user
    """
    return current_app.auth_mgr.login_user(user)


def logout():
    """
    Logs the user out
    """
    return current_app.auth_mgr.logout()


def register_authentication_manager(app, login_view,
    login_message='Please login to access this page.',
    login_message_category='message'):
    """
    Registers the autn manager with the app
    """
    auth_mgr = AuthenticationManager(app, login_view,
        login_message=login_message,
        login_message_category=login_message_category)
    app.login_manager = auth_mgr

    # make the account available to everyone
    @app.before_request
    def setup_request():
        if is_logged_in():
            g.user = get_user_by_id(request.db, get_logged_in_user_id())
            if not g.user:
                logout()
                return


class AuthenticationManager(object):

    def __init__(self, app,
        login_view=None, login_message=None, login_message_category=None):
        app.auth_mgr                = self
        self.login_view             = login_view
        self.login_message          = login_message
        self.login_message_category = login_message_category

    def logout(self):
        """
        Logs the user out
        """
        if session.has_key("userId"):
            del session["userId"]

    def unauthorized(self):
        """
        Called when a user tries to access something
        that they aren't authorized to
        """
        if not self.login_view:
            abort(401)
        if self.login_message:
            flash(self.login_message, category=self.login_message_category)
        return redirect(url_for(self.login_view))

    def login_user(self, user):
        """
        Logs in the user
        """
        # log them in
        session['userId'] = user.get('_id')
        g.user = user
        return user

    def login(self, login, password):
        """
        Performs authentication
        """
        # call auth method
        user = get_user_by_username(request.db, login)
        if not md5(password).hexdigest() == user.get('password_hash'):
            return None

        return self.login_user(user)
