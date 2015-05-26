
from flask import Blueprint

#create Blueprint
homepage_blueprint = Blueprint('homepage', __name__,
                               static_folder='assets',
                               template_folder='templates')



#ho0k up da views mang
from . import views
