
class Farm:
    def __init__(self, market_name,):
        self.name = market_name
        self.stock = []
    def add_animal(self, animal_name, num):
        if animal_name in self.stock:
            #seulement aditionner le num
            a=num
        else:
            self.stock.append(animal_name)
            self.stock.append(num)
    def get_info(self):
        print("gg") #print se qu'il y a dans la stock
    def get_animal_types(self):
        print("ok") # return all name of animals
    def get_short_info(self):
        
    


