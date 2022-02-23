"""
A distance class will cacluate the distance the send back results in KM
"""
import math


class Distance:
    def __init__(self, origin, destination):
        self.origin = []
        self.destination = []

    def distance(self, origin, destination):
        lat1, lon1 = origin
        lat2, lon2 = destination
        radius = 6371  # km

        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) \
            * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = radius * c
        return d

    # Asks the user for the distance in either miles or kilometers
    def unit_distance_select(self):
        selection = input("please enter a unit of distance\n M (miles) K(Kilometers)")
        while selection.lower() not in ['m', 'k']:
            selection = input("Please Try again, M (miles) or K (Kilometers)\n")

        if selection.lower() == 'k':
            return 'kilometers'
        else:
            return 'miles'
