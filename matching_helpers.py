#from geopy.geocoders import OpenCage
#from geopy.distance import geodesic
import json

AGE_THRESHOLD = 3

# def get_coordinates(location, geolocator):
#     try:
#         location = geolocator.geocode(location)

#     except Exception:
#       return "Please input the address in correct format"

#     return (location.latitude, location.longitude)

# def get_distance(location1, location2, geolocator):
#     coords_1 = get_coordinates(location1, geolocator)
#     coords_2 = get_coordinates(location2, geolocator)
#     distance = geodesic(coords_1, coords_2).kilometers

#     return distance

def get_age_score(users_age, age_low, age_high):
    if users_age >= age_low and users_age <= age_high:
        return 1
    elif users_age < age_low and users_age + AGE_THRESHOLD > age_low:
        return 0.5
    elif users_age > age_high and users_age - AGE_THRESHOLD < age_high:
        return 0.5
    else:
        return 0
    
def get_interests_score(users_interests, interests):
    intersect = len(set(users_interests).intersection(interests))
    union = len(set(users_interests).union(interests))
    return intersect/union

#The Json file contains the score calculated for each pair of Ontario cities.  
#The score is calculated by 1/x, x is the distance between two cities in km. 
#The city pair is ranked by their score value.
with open('cities_ranked.json', 'r') as json_file:
    distance_score = json.load(json_file)

# The cut-off line is 80km, run Geolocation.py to see the box-plot and the distribution plot of distances beyond 80km.
# The cut-off is intended to seperate the cities that are close to each other (<71km)
# Give the appropriate weight to the cities that are far from each other (>71km) by normalizing the score.

distance_score_1 = dict(list(distance_score.items())[:87]) 
distance_score_2 = dict(list(distance_score.items())[87:])

max_score = max(distance_score_2.values())
min_score = min(distance_score_2.values())

# Normalize the score
for key in distance_score_2:
    normalized_score = (distance_score_2[key] - min_score) / (max_score - min_score)
    distance_score_2[key] = normalized_score

def get_location_score(users_location, location):
    name_1 = f'{users_location} - {location}'
    name_2 = f'{location} - {users_location}'# Alternative name for city pair
    
    if users_location == location or name_1 in distance_score_1 or name_2 in distance_score_1: # If the two cities are close to each other
        return 1
    else:
        try:
            score = distance_score_2[f'{users_location} - {location}']
            return score
        except KeyError:
            try:
            # If that fails, try the reverse combination
                score = distance_score_2[f'{location} - {users_location}']
                return score
            except KeyError:
            # Handle the case where neither key is found
                print(f"Warning: No distance score found for {users_location} and {location}")
                return 0

        
