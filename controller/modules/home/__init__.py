from flask import Blueprint

home_blu = Blueprint("home", __name__)

from controller.modules.home.views import *
