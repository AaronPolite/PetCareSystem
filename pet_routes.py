from flask import Blueprint, request, jsonify
from app.services.pet_service import add_pet, delete_pet

pet_routes = Blueprint('pet_routes', __name__)

@pet_routes.route('/pets', methods=['POST'])
def create_pet():
    data = request.get_json()
    pet = add_pet(data['name'], data['species'], data['owner_id'])
    return jsonify(pet), 201

@pet_routes.route('/pets/<int:pet_id>', methods=['DELETE'])
def remove_pet(pet_id):
    delete_pet(pet_id)
    return jsonify({"message": "Pet deleted successfully"}), 200
