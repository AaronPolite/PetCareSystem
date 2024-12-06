#User class that handles the creation and modification of information of a user object
class User:
    #Constants to handle Indexing
    LAST_NAME_INDEX = 0
    FIRST_NAME_INDEX = 1
    EMAIL_INDEX = 2
    PHONE_NUMBER_INDEX = 3
    PETS_INDEX = 4

    def __init__(self, last_name, first_name, email, phone_number, pets):
        self.details = [last_name, first_name, email, phone_number, pets]

    def get_last_name(self):
        return self.details[self.LAST_NAME_INDEX]

    def get_first_name(self):
        return self.details[self.FIRST_NAME_INDEX]

    def get_email(self):
        return self.details[self.EMAIL_INDEX]
    
    def get_phone_number(self):
        return self.details[self.PHONE_NUMBER_INDEX]

    def get_pets(self):
        return self.details[self.PETS_INDEX]
    
    def set_last_name(self, last_name):
        self.details[self.LAST_NAME_INDEX] = last_name

    def set_first_name(self, first_name):
        self.details[self.FIRST_NAME_INDEX] = first_name

    def set_phone_number(self, phone_number):
        self.details[self.PHONE_NUMBER_INDEX] = phone_number

    def set_email(self, email):
        self.details[self.EMAIL_INDEX] = email

    def set_pets(self, pets_list):
        self.details[self.PETS_INDEX] = pets_list
        