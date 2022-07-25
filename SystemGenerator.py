'''
Generates a random system for my Starfinder Campaign
'''
from random import randint
from Planet import Planet


class SystemGenerator:

    telluric_planets = list()
    gas_giants = list()
    possible_star_classes = ["B", "A", "F", "G", "K", "M", "M Red Giant", "T Brown Dwarf"]
    exotic_star_classes = ["pulsar", "neutron", "black hole"]
    star_class = ""
    star_name = ""


    # stars can be B, A, F, G, K, M, MRG(M red giant), TBD(T brown dwarf), pulsar, neutron, black hole
    def __init__(self, star_name="", star_class=None, use_exotic_stars=False, generate_planets=True,
                 min_telluric_planets=0, max_telluric_planets=5, min_gas_giants=0, max_gas_giants=5):
        self.star_name = star_name
        if use_exotic_stars:
            self.star_class = self.exotic_star_classes[randint(0, len(self.exotic_star_classes)-1)]
        elif star_class is not None:
            self.star_class = self.possible_star_classes
        else:
            self.star_class = self.possible_star_classes[randint(0, len(self.possible_star_classes)-1)]

        # give some planets
        if (self.star_class != "black hole") and generate_planets:
            self.telluric_planets = [Planet() for i in range(randint(min_telluric_planets, max_telluric_planets))]
            # gas giants typically have many more moons
            self.gas_giants = [Planet(is_gas_giant=True, max_moons=5) for i in range(randint(min_gas_giants, max_gas_giants))]


    def __str__(self):
        system_str = ""

        if self.star_name != "":
            system_str += "Star Name: " + self.star_name + "\n"

        system_str += "Class: " + self.star_class + "\n"

        if self.telluric_planets != [] or self.gas_giants != []:
            system_str += "Planets: \n"
            for telluric_planet in self.telluric_planets:
                system_str += telluric_planet.to_formatted_str(deepness=1)
            for gas_giant in self.gas_giants:
                system_str += gas_giant.to_formatted_str(deepness=1)

        system_str += "\nQuick Summary of Planets\nNumber of Telluric planets: " + str(len(self.telluric_planets)) \
                      + "\nNumber of Gas giants: " + str(len(self.gas_giants))

        return system_str


if __name__ == '__main__':
    star_name = "Rigel"
    system = SystemGenerator(star_name)
    print(system)
    with open(star_name+".txt", "w") as f:
        f.write(str(system))