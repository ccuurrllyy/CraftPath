import numpy as np
from numpy import inf
import requests
from django.conf import settings
from .route_algorithm import main

def get_best_path_and_cost(addresses):
    distances_array = create_distances_array(addresses)
    best_path, cost_of_best_path = main(distances_array)
    return best_path, cost_of_best_path


def create_distances_array(addresses): #function for creating thre distance
    distances_array = []
    for origin in addresses:
        origin_param = str(origin.location.y) + "," + str(origin.location.x)
        destinations_param = ''
        for destination in addresses:
            if destination != addresses.first():
                destinations_param += "|"

            destinations_param += str(destination.location.y) + "," + str(destination.location.x)

        # print(origin_param, destinations_param)
        origin_array = get_google_distance_matrix_results(origin_param, destinations_param)
        distances_array.append(origin_array)
    print(distances_array)
    return distances_array



def get_google_distance_matrix_results(origin, destinations):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    url += "?origins=" + origin
    url += "&destinations=" + destinations
    url += "&key=" + settings.GOOGLE_GEOCODE_API_KEY

    resp = requests.get(url)
    distances = []
    if resp.status_code == 200:
        s = resp.json()
        distances = [item['distance']['value'] for item in s['rows'][0]['elements']]

    return distances
