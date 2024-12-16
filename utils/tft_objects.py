
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
    
    def get_traits(self):
        return self.traits
    
    
class Teams:
    team_name = ""
    champs = []
    synergies = {}

    def __init__(self, team_name, champs):
        self.team_name = team_name
        self.champs = champs
        synergies = self.calculate_synergy(champs)

    def __str__(self):
        return f"{self.team_name} : {", ".join(self.champs)} --- Synergies: {self.synergy_string(self.champs)}"

    def synergy_string(self, champs):   # returns a a pretty string of synergy dictionary
        s_str = f""
        return s_str
        

    def calculate_synergy(self,champs):     # returns modified synergy dictionary  --- key: trait , val: freq of trait
        for c in champs:    #iterate through the champ list, update synergy when new trait encountered, add 1 to existing traits
            for t in c.get_traits():
                self.synergies[t] = self.synergies.get(t,0) + 1

        return self.synergies

    def set_team_name(self, new_name):
        self.team_name = new_name

    def reset_team(self, champs, synergies):
        self.champs = []
        self.synergies = {}

