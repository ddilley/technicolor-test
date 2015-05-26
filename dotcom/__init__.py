
from flask import Flask, request, url_for, render_template
from test_lib.flask import force_scheme

# create app
app = Flask('test_dotcom')
from test_lib.config.appConfig import register_config
register_config(app)

# setup cache
from flask.ext.cache import Cache
app.cache = Cache(app)

# setup session management
from pressed_lib.flask.session import register_cache_session_handler
register_cache_session_handler(app, cache=app.cache)

# Define database access.
from test_lib.data import register_db_session
register_db_session(app)

# register login manager
from flask.ext.login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)


@app.before_request
def before_r():
  pass

@app.after_request
def after_r(response):
  return response

@app.route('/python')
def python_version():
    return "Python version: "+str(sys.version_info)


# import blueprints
from blueprints.homepage import homepage_blueprint

# register blueprints
app.register_blueprint(homepage_blueprint, url_prefix='/')

# Import asset bundles.
from test_dotcom.bundles import register_bundles
register_bundles(app)
