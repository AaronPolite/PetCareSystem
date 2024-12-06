class Pet:
    def __init__(self, name, species, age=int, bills=dict, visits=dict):
        self.details = [name, species, age, bills, visits]

    def get_name(self):
        return self.details[0]

    def get_species(self):
        return self.details[1]

    def get_age(self):
        return self.details[2]
    
    def get_bills(self):
        return self.details[3]

    def get_visits(self):
        return self.details[4]
    
    def set_name(self, name):
        self.details[0] = name

    def set_species(self, species):
        self.details[1] = species

    def set_age(self, age=int):
        self.details[2] = age

    def set_bills(self, bills=dict):
        self.details[3] = bills

    def set_visits(self, visits=dict):
        self.details[4] = visits