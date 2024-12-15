
class Champions:
    name = ""
    cost = 0
    traits = []
    image_path = ""

    def __init__(self, name, cost, traits, image_path):
        self.name = name
        self.cost = cost
        self.traits = traits
        self.image_path = image_path

    def __str__(self):
        return (f"{self.name} (Cost: {self.cost}, Traits: {', '.join(self.traits)})")
    
    