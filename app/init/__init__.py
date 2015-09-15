from flask import Blueprint

init = Blueprint('init', __name__)

from . import views