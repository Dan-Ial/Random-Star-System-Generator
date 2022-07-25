'''
Generates a random system for my Starfinder Campaign
'''
from random import randint
import Planet

class SystemGenerator:

    telluric_planets = []
    gas_giants = []
    astroid_belt = False
    possible_star_classes = ["B", "A", "F", "G", "K", "M", "MRG", "TBD"]
    exotic_star_classes = ["pulsar", "neutron", "black hole"]
    star_class = ""
    star_name = ""


    # stars can be B, A, F, G, K, M, MRG(M red giant), TBD(T brown dwarf), pulsar, neutron, black hole
    def __init__(self, star_name, star_class=None, use_exotic_stars=False, generate_planets_and_asteroids=True):
        self.star_name = star_name
        if use_exotic_stars:
            self.star_class = self.exotic_star_classes[randint(0, len(self.exotic_star_classes))]
        elif star_class is not None:
            self.star_class = self.possible_star_classes
        else:
            self.star_class = self.possible_star_classes[randint(0, len(self.possible_star_classes))]




    def __str__(self):
        return


if __name__ == '__main__':
    print(SystemGenerator("Rigel"))