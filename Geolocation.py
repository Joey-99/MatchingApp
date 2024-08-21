from geopy.geocoders import OpenCage
from geopy.distance import geodesic
import itertools
import json

# Replace 'YOUR_API_KEY' with your actual OpenCage API key
geolocator = OpenCage(api_key='00f4aaf4afff4e268c8e172fb70366d4')

def get_coordinates(location):
    try:
        location = geolocator.geocode(location)

        return (location.latitude, location.longitude)


    except Exception as e:
        print(f"The error is {e}")
        return "Please input the address in correct format"

def get_distance(coords_1, coords_2):

    try:
      distance = geodesic(coords_1, coords_2).kilometers

      #return f"The distance between {location1} and {location2} is {distance:.2f} kilometers."
      return distance

    except Exception:
      return None
    
def iterate_pairwise(cities):
    pairs = list(itertools.combinations(cities, 2))
    return pairs

def write_dict_to_json(dictionary, filename):
    with open(filename, 'w') as json_file:
        json.dump(dictionary, json_file, indent=4)
    

cities = [
    "Toronto",
    "Ottawa",
    "Mississauga",
    "Brampton",
    "Hamilton",
    "London",
    "Markham",
    "Vaughan",
    "Kitchener",
    "Windsor",
    "Richmond Hill",
    "Burlington",
    "Oshawa",
    "Greater Sudbury",
    "Barrie",
    "Guelph",
    "Cambridge",
    "St. Catharines",
    "Waterloo",
    "Thunder Bay",
    "Brantford",
    "Pickering",
    "Niagara Falls",
    "Peterborough",
    "Sault Ste. Marie",
    "Sarnia",
    "Norfolk County",
    "Welland",
    "Belleville",
    "North Bay"
]

coordinates = {}
score_dict = {}
city_pairs = iterate_pairwise(cities)
city_pairs = city_pairs[0:4]
counter = 0

# #Retrive the coordinates of each city
# for city in cities:
#   city_name = city + ",Ontario"
#   print(city_name)
#   latitude, longitude = get_coordinates(city_name)
#   coordinates[city] = (latitude, longitude)

# #Calculate the distance between each pair of cities and convert it to score
# for city_pair in city_pairs:
#   distance = get_distance(coordinates[city_pair[0]],coordinates[city_pair[1]])
#   score_dict[f"{city_pair[0]} - {city_pair[1]}"] = 1/distance
#   counter +=1
#   print(f"{counter} out of {len(city_pairs)} has done")

# Read json file
with open('cities.json', 'r') as json_file:
    score_dict = json.load(json_file)

# Normalize the result value in score_dict
max_score = max(score_dict.values())
max_score_keys = [key for key, value in score_dict.items() if value == max_score]

# print(max_score_keys)
# print(max_score)

# sorted_scores = sorted(score_dict.values(), reverse=True)
# second_highest_score = sorted_scores[1]

# second_highest_score_keys = [key for key, value in score_dict.items() if value == second_highest_score]
# print(f"The second highest score is {second_highest_score} with keys: {second_highest_score_keys}")


min_score = min(score_dict.values())
# print(min_score)
# print(len(score_dict))

for key in score_dict:
    normalized_score = (score_dict[key] - min_score) / (max_score - min_score)
    score_dict[key] = normalized_score

#print(score_dict)

highest_score_key = [key for key, value in score_dict.items() if value == 1]

write_dict_to_json(score_dict, 'cities.json')
