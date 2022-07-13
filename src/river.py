class River:
    def __init__(self, name, river_fish):
        self.name = name
        self.river_fish = river_fish

    def count_fish_in_river(self):
        return len(self.river_fish)

    def remove_fish_in_river(self):
        del(self.river_fish[0])

    