"""
A city class will ask user for city and return a list of dictionary values of a city.
"""
import geonamescache
class City:
    def __init__(self):
        self.city = []

    def ask_for_city(self):
        gc = geonamescache.GeonamesCache()
        city = []
        while len(city) == 0:
            selection = input("please enter a city:\n")
            selection = selection[0].upper() + selection[1:].lower()
            city = gc.search_cities(selection)

        if (len(city) > 1):  # was there more than 1 city for the search
            print("multiple locations appeared, Please select from this list")
            locationlist = []
            newvalues = {}
            finalcity = []
            for city_id, city_values in enumerate(city):
                for key in city_values:
                    if key in ('name', 'countrycode', 'timezone'):
                        newvalues[key] = city_values[key]
                locationlist.append((newvalues))
                newvalues = {}

            for count, value in enumerate(locationlist):
                print("{} : = {}".format(count, value))
            num_of_locations = []
            for count in range(len(locationlist)):
                num_of_locations.append(count)

            selection = input()
            while int(selection) not in num_of_locations:
                selection = input("please select a location{}".format(num_of_locations))
            finalcity.append(city[int(selection)])
            # print(finalcity)
            return finalcity

        else:
            # print(city)
            return city
