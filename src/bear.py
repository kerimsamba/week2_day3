class Bear:
    def __init__(self, name, stomach):
        self.name = name
        self.stomach = stomach
    
    def eat_fish(self, a_fish):
        self.stomach.append(a_fish.name)

    def food_count(self):
        return len(self.stomach)