
from flask import Flask, request, url_for, render_template

# create app
app = Flask('test_dotcom', static_folder='dotcom/static', template_folder='dotcom/templates')

# register the configuration
from test_lib.config.appConfig import register_config
register_config(app)

# Define database access.
from test_lib.data import register_db_session
register_db_session(app)

# register login manager
from test_lib.flask.login import register_authentication_manager
register_authentication_manager(app, 'homepage.login')


"""
@app.before_request
def before_r():
  pass

@app.after_request
def after_r(response):
  return response
"""

@app.route('/python')
def python_version():
    return "Python version: "+str(sys.version_info)


# import blueprints
from blueprints.homepage import homepage_blueprint

# register blueprints
app.register_blueprint(homepage_blueprint, url_prefix='/')

# Import asset bundles.
from dotcom.bundles import register_bundles
register_bundles(app)






