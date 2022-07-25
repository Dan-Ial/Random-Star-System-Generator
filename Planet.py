'''
Generates a random planet for my Starfinder Campaign
'''

from random import randint, uniform, choices, seed

class Planet:

    body_type = str()
    planet_type = str()
    moons = []
    size = int()                # in Earths

    def __init__(self, is_gas_giant=False, is_moon=False, size_lower_limit=0.66, size_upper_limit=1.38, min_moons=0, max_moons=2, overriding_moon_size=False):
        if is_gas_giant:
            self.body_type = "Gas Giant"

            # give some moons
            self.moons = [Planet(is_moon=True) for i in range(randint(min_moons, max_moons))]

        elif is_moon:
            self.body_type = "Moon"

            # generate the planet type
            planet_type_weights = {
                "Barren": 15.5,
                "Barren Cold": 15.5,
                "Broken": 15.5,
                "Frozen": 15.5,
                "Molten": 15.5,
                "Toxic": 15.5,
                "Habitable": 7
            }
            habitable_type_weights = {
                "Habitable Arid": 9.44,
                "Habitable Desert": 9.44,
                "Habitable Savanna": 9.44,
                "Habitable Alpine": 9.44,
                "Habitable Arctic": 9.44,
                "Habitable Tundra": 9.44,
                "Habitable Continental": 9.44,
                "Habitable Ocean": 9.44,
                "Habitable Tropical": 9.44,
                "Habitable Gaia": 5,
                "Habitable Tomb": 5,
                "Habitable Relic": 5
            }

            planet_type = choices(list(planet_type_weights.keys()), list(planet_type_weights.values()))

            if planet_type[0] == "Habitable":
                planet_type = choices(list(habitable_type_weights.keys()), list(habitable_type_weights.values()))

            self.planet_type = planet_type[0]

            # generate the size
            if overriding_moon_size:
                moon_size_lower_limit = size_lower_limit
                moon_size_upper_limit = size_upper_limit
            else:
                moon_size_lower_limit = 0.20
                moon_size_upper_limit = 0.55

            self.size = round(uniform(moon_size_lower_limit, moon_size_upper_limit), 2)

        else:
            self.size = round(uniform(size_lower_limit, size_upper_limit), 2)
            self.body_type = "Telluric"

            # generate the planet type
            planet_type_weights = {
                "Barren": 15.5,
                "Barren Cold": 15.5,
                "Broken": 15.5,
                "Frozen": 15.5,
                "Molten": 15.5,
                "Toxic": 15.5,
                "Habitable": 7
            }
            habitable_type_weights = {
                "Habitable Arid": 9.44,
                "Habitable Desert": 9.44,
                "Habitable Savanna": 9.44,
                "Habitable Alpine": 9.44,
                "Habitable Arctic": 9.44,
                "Habitable Tundra": 9.44,
                "Habitable Continental": 9.44,
                "Habitable Ocean": 9.44,
                "Habitable Tropical": 9.44,
                "Habitable Gaia": 5,
                "Habitable Tomb": 5,
                "Habitable Relic": 5
            }

            planet_type = choices(list(planet_type_weights.keys()), list(planet_type_weights.values()))

            if planet_type[0] == "Habitable":
                planet_type = choices(list(habitable_type_weights.keys()), list(habitable_type_weights.values()))

            self.planet_type = planet_type[0]

            # give some moons
            self.moons = [Planet(is_moon=True) for i in range(randint(min_moons, max_moons))]


    def to_formatted_str(self, deepness=0):
        planet_str = ""
        planet_str += str("| "*deepness) + "\n"  # extra whitespace
        planet_str += str("| "*deepness) + "Body Type: " + self.body_type + "\n"
        if self.body_type != "Gas Giant":
            planet_str += str("| "*deepness) + "Planet Type: " + str(self.planet_type) + "\n"
            planet_str += str("| "*deepness) + "Size: " + str(self.size) + " Earths" +"\n"

        if self.moons != []:
            for moon in self.moons:
                planet_str += moon.to_formatted_str(deepness+1)


        return planet_str


    def __str__(self):
        return self.to_formatted_str()







if __name__ == '__main__':
    planet_test = Planet()
    print(planet_test)