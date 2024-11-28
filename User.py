
#User class that handles the creation and modification of information of a user object
class User:
    #Constants to handle Indexing
    NAME_INDEX = 0
    ID_INDEX = 1
    POSITION_INDEX = 2
    EMAIL_INDEX = 3
    ADDITIONAL_INDEX = 4

    def __init__(self, name, employee_id, position, email, additional):
        self.details = [name, employee_id, position, email, additional]

    def get_name(self):
        return self.details[self.NAME_INDEX]

    def get_user_id(self):
        return self.details[self.ID_INDEX]

    def get_position(self):
        return self.details[self.POSITION_INDEX]
    
    def get_email(self):
        return self.details[self.EMAIL_INDEX]

    def get_additional(self):
        return self.details[self.ADDITIONAL_INDEX]
    
    def set_name(self, name):
        self.details[self.NAME_INDEX] = name

    def set_user_id(self, id):
        self.details[self.ID_INDEX] = id

    def set_position(self, position):
        self.details[self.POSITION_INDEX] = position

    def set_email(self, email):
        self.details[self.EMAIL_INDEX] = email

    def set_additional(self, additional):
        self.details[self.ADDITIONAL_INDEX] = additional
