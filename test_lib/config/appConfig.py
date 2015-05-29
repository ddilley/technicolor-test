
import os

"""
    An example of how we might manage environment configurations
"""

# Base settings
class Config(object):
    DEBUG                       = False
    ASSETS_DEBUG                = False
    ENABLE_SCHEME_ENFORCEMENT   = True
    SESSION_COOKIE_NAME         = '_cs'
    SECRET_KEY                  = 'seceret_sauce'
    pass

# Production
class ProductionConfig(Config):
    pass

# Development
class DevelopmentConfig(Config):
    DEBUG                       = True
    ASSETS_DEBUG                = True
    ENABLE_SCHEME_ENFORCEMENT   = False
    pass

# QA
class QaConfig(Config):
    NABLE_SCHEME_ENFORCEMENT   = False
    pass


def getConfig():
    # setup environment
    if not os.environ.has_key("PROJECT_ENV_NAME"):
        os.environ["PROJECT_ENV_NAME"] = "dev"
    # register the configuration
    if os.environ["PROJECT_ENV_NAME"] == "dev":
        return DevelopmentConfig
    elif os.environ["PROJECT_ENV_NAME"] == "qa":
        return QaConfig
    elif os.environ["PROJECT_ENV_NAME"] == "prod":
        return ProductionConfig
    else:
        raise Exception("Unable to determine PRESSED_ENV_NAME")


def register_config(app):
    conf = getConfig()
    app.config.from_object('%s.%s' % (conf.__module__, conf.__name__))
