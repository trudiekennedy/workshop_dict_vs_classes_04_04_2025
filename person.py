class Person:
    def __init__(self, name, hobbies):
        self.name = name
        self.hobbies = hobbies
    
    def print_hobbies(self):
        for hobby in self.hobbies:
            print(hobby)
        return "Hobbies printed"
    
    def print_name(self):
        print(self.name)
        return "name printed"