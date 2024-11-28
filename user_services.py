from app.models import db, User

def add_user(userid, name, password, is_admin=False):
    if User.query.filter_by(userid=userid).first():
        raise ValueError("User ID already exists")
    new_user = User(userid=userid, name=name, is_admin=is_admin)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return new_user.to_dict()

def get_user_by_userid(userid):
    user = User.query.filter_by(userid=userid).first()
    if not user:
        raise ValueError("User not found")
    return user.to_dict()

def update_user_as_admin(admin_id, target_userid, new_data):
    admin = User.query.get(admin_id)
    if not admin or not admin.is_admin:
        raise PermissionError("Only admins can update user data")
    target_user = User.query.filter_by(userid=target_userid).first()
    if not target_user:
        raise ValueError("Target user not found")
    target_user.name = new_data.get('name', target_user.name)
    if 'password' in new_data:
        target_user.set_password(new_data['password'])
    db.session.commit()
    return target_user.to_dict()

def delete_user(userid):
    user = User.query.filter_by(userid=userid).first()
    if not user:
        raise ValueError("User not found")
    db.session.delete(user)
    db.session.commit()
