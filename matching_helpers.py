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


with open('cities.json', 'r') as json_file:
    distance_score = json.load(json_file)

def get_location_score(users_location, location):
    if users_location == location:
        return 1
    else:
        try:
            score = distance_score[f'{users_location} - {location}']
            return score
        except KeyError:
            try:
            # If that fails, try the reverse combination
                score = distance_score[f'{location} - {users_location}']
                return score
            except KeyError:
            # Handle the case where neither key is found
                print(f"Warning: No distance score found for {users_location} and {location}")
                return 0

        
