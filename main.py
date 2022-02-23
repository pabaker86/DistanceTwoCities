"""
Distance Between Two Cities - Calculates the distance between two cities
and allows the user to specify a unit of distance.
This program may require finding coordinates for the cities like latitude and longitude.
"""

from city import City
from distance import Distance


#calling the main script for the program.
if __name__ == '__main__':
    origin = []
    destination = []
    dist = Distance(origin, destination)
    city = City()
    print('Distance between Cities!\n')
    selection = dist.unit_distance_select()
    #print(selection)

    city1 = city.ask_for_city()
    for key, values in enumerate(city1):
        print("City = {}, Latitude = {}, Longitude = {}".format(city1[0]['name'], city1[0]['latitude'], city1[0]['longitude']))
        origin = [city1[0]['latitude'], city1[0]['longitude']]

    city2 = city.ask_for_city()
    for key, values in enumerate(city2):
        print("City = {}, Latitude = {}, Longitude = {}".format(city2[0]['name'], city2[0]['latitude'], city2[0]['longitude']))
        destination = [city2[0]['latitude'], city2[0]['longitude']]


    total_distance = dist.distance(origin, destination)

    if selection.upper() == 'KILOMETERS':
         print("Total distance in Kilometers is {}".format(round(total_distance, 2)))
    elif selection.upper() == 'MILES':
        conv_fac = 0.621371 # conversion factor
        # calculate miles
        miles = total_distance * conv_fac
        print('Total distance between {} and {} in Miles is {}'.format(city1[0]['name'], city2[0]['name'], round(miles, 2)))

