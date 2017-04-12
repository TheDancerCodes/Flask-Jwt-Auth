# project/server/auth/views.py

from flask import Blueprint, request, make_response, jsonify
from flask.views import Methodiew

from project.server import bcrypt, db
from project.server.models import User

auth_blueprint = Blueprint('auth', __name__)
