import unittest

from src.fish import Fish
from src.river import River
from src.bear import Bear

class TestEcosystem(unittest.TestCase):

    def setUp(self):
        
        self.bear = Bear("Yogi", [])
        self.fish = Fish("Nemo")
        fish1 = Fish("Flipper")
        fish2 = Fish("Herbert")
        fish3 = Fish("Jaws")
        fish4 = Fish("Sammy")
        self.river = River("The Yukon", [fish1, fish2, fish3, fish4])

    def test_fish_has_name(self):
        self.assertEqual("Nemo", self.fish.name)

    def test_bear_has_name(self):
        self.assertEqual("Yogi", self.bear.name)

    def test_bear_has_empty_stomach(self):
        self.assertEqual(0, len(self.bear.stomach))

    def test_bear_can_eat_fish(self):
       self.bear.eat_fish(self.fish)
       self.assertEqual("Nemo", self.bear.stomach[0])

    def test_bear_stomach_count(self):
       self.bear.eat_fish(self.fish)
       self.assertEqual(1, self.bear.food_count())

    def test_river_has_name(self):
        self.assertEqual("The Yukon", self.river.name)

    def test_river_has_many_fish(self):
        self.assertEqual(4, len(self.river.river_fish))

    def test_counting_fish_method(self):
        self.assertEqual(4, self.river.count_fish_in_river())

    def test_bear_taking_a_fish(self):
        self.bear.eat_fish(self.river.river_fish[0])
        self.assertEqual("Flipper", self.bear.stomach[0])
        self.river.remove_fish_in_river()
        self.assertEqual(3, self.river.count_fish_in_river())
        


