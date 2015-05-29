
from flask.ext.assets import Environment, Bundle

"""
    An example of how we might bundle assets
"""

def register_bundles(app):
    assets = Environment(app)
    assets.debug = app.config.get('ASSETS_DEBUG', False)

    ##
    # CSS
    css_global = Bundle(
        'css/shared/normalize.scss',
        'css/global.scss',
        filters='scss, cssmin',
        output='gen/global.css')
    assets.register('css_global', css_global)

    css_home = Bundle(
        'css/home.scss',
        filters='scss, cssmin',
        #otheCssBundled
        output='gen/home.css')
    assets.register('css_home', css_home)

    ##
    # Javascript
    js_global = Bundle('js/jquery-1.9.1.js', 'js/global.js','js/someUtil.js')
    js_global = Bundle(
        Bundle(js_global),
         #otherJsBundled,
        output='gen/script.js'
    )
    assets.register('js_global', js_global)
