import json
import pandas as pd
import numpy as np

def write_dict_to_json(dictionary, filename):
    with open(filename, 'w') as json_file:
        json.dump(dictionary, json_file, indent=4)

# Read json file
with open('cities_old.json', 'r') as json_file:
    score_dict = json.load(json_file)

sorted_list = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)
sorted_dict = dict(sorted_list)

# Divide the sorted_dict into five parts evenly
n = len(sorted_dict)
part_size = n // 5
parts = [list(sorted_dict.items())[i:i+part_size] for i in range(0, n, part_size)]

# Create a list to store the box plot data
box_plot_data = []

# Iterate over each part and extract the inverse distances
for part in parts:
    distances = [1/inverse_distance for _, inverse_distance in part]
    box_plot_data.append(distances)

Intracities_distance = [1/inverse_distance for cities, inverse_distance in list(sorted_dict.items())[80:87]]
Cities = [cities for cities, inverse_distance in list(sorted_dict.items())[80:87]]
Intra_cities = pd.DataFrame({'Cities': Cities, 'Distance': Intracities_distance})

Intercities_score = [inverse_distance for cities, inverse_distance in list(sorted_dict.items())[87:]]