from flask import Blueprint, request, jsonify
from app.services.user_service import add_user, get_user_by_userid, update_user_as_admin

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = add_user(data['userid'], data['name'], data['password'], data.get('is_admin', False))
    return jsonify(user), 201

@user_routes.route('/users/<string:userid>', methods=['GET'])
def get_user(userid):
    user = get_user_by_userid(userid)
    return jsonify(user), 200

@user_routes.route('/users/<string:target_userid>', methods=['PUT'])
def update_user(target_userid):
    data = request.get_json()
    admin_id = data.get('admin_id')
    user = update_user_as_admin(admin_id, target_userid, data)
    return jsonify(user), 200
