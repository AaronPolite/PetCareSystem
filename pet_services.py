from app.models import db, Pet, User

def add_pet(name, species, owner_id):
    owner = User.query.get(owner_id)
    if not owner:
        raise ValueError("Owner not found")
    new_pet = Pet(name=name, species=species, owner_id=owner_id)
    db.session.add(new_pet)
    db.session.commit()
    return new_pet.to_dict()

def delete_pet(pet_id):
    pet = Pet.query.get(pet_id)
    if not pet:
        raise ValueError("Pet not found")
    db.session.delete(pet)
    db.session.commit()
