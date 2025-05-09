ORBITAL_PERIOD = {
    "mercury":	0.2408467,
    "venus":	0.61519726,
    "earth":	1.0,
    "mars":	1.8808158,
    "jupiter":	11.862615,
    "saturn":	29.447498,
    "uranus":	84.016846,
    "neptune":	164.79132
}
EARTH_SECONDS_IN_YEAR = 3600 * 24 * 365.25
class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def on_mercury(self):
        return round(self.seconds / (EARTH_SECONDS_IN_YEAR * ORBITAL_PERIOD["mercury"]), 2)

    def on_venus(self):
        return round(self.seconds / (EARTH_SECONDS_IN_YEAR * ORBITAL_PERIOD["venus"]), 2)


    def on_earth(self):
        return round(self.seconds / EARTH_SECONDS_IN_YEAR, 2)


    def on_mars(self):
        return round(self.seconds / (EARTH_SECONDS_IN_YEAR * ORBITAL_PERIOD["mars"]), 2)

    def on_jupiter(self):
        return round(self.seconds / (EARTH_SECONDS_IN_YEAR * ORBITAL_PERIOD["jupiter"]), 2)

    def on_saturn(self):
        return round(self.seconds / (EARTH_SECONDS_IN_YEAR * ORBITAL_PERIOD["saturn"]), 2)

    def on_uranus(self):
        return round(self.seconds / (EARTH_SECONDS_IN_YEAR * ORBITAL_PERIOD["uranus"]), 2)

    def on_neptune(self):
        return round(self.seconds / (EARTH_SECONDS_IN_YEAR * ORBITAL_PERIOD["neptune"]), 2)
        

print(SpaceAge(50 * 365.2425 * 24 * 3600).on_earth())
print(SpaceAge(2134835688).on_mercury())
print(SpaceAge(50 * 365.2425 * 24 * 3600).on_venus())
print(SpaceAge(50 * 365.2425 * 24 * 3600).on_mars())
print(SpaceAge(50 * 365.2425 * 24 * 3600).on_jupiter())
print(SpaceAge(50 * 365.2425 * 24 * 3600).on_saturn())
print(SpaceAge(50 * 365.2425 * 24 * 3600).on_saturn())
print(SpaceAge(50 * 365.2425 * 24 * 3600).on_uranus())
print(SpaceAge(50 * 365.2425 * 24 * 3600).on_neptune())
print(2134835688 / ((3600 * 24 * (365.256)) * 0.2408467))

# print(ORBITAL_PERIOD)""


