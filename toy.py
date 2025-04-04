class Toy:
    def __init__(self, dict):
        self.toy_dict = dict

    def return_name(self):
        print([toy['name'] for toy in self.toy_dict])
    
    def return_colour(self):
        print([toy['colour'] for toy in self.toy_dict])