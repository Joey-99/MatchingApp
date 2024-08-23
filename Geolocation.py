import json
import pandas as pd

def write_dict_to_json(dictionary, filename):
    with open(filename, 'w') as json_file:
        json.dump(dictionary, json_file, indent=4)

# Read json file
with open('cities_old.json', 'r') as json_file:
    score_dict = json.load(json_file)

# Sort the dictionary by values
sorted_list = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)
sorted_dict = dict(sorted_list)


# Divide the sorted cities distance into five quantiles
n = len(sorted_dict)
part_size = n // 5
parts = [list(sorted_dict.items())[i:i+part_size] for i in range(0, n, part_size)]

# Create a list to store the box plot data
box_plot_data = []

# Iterate over each part and extract the inverse distances
for part in parts:
    distances = [1/inverse_distance for _, inverse_distance in part]
    box_plot_data.append(distances)

# Print the cities that are closer than 71km
# Intracities_distance = [1/inverse_distance for cities, inverse_distance in list(sorted_dict.items())[0:87]]
# Cities = [cities for cities, inverse_distance in list(sorted_dict.items())[0:87]]
# Intra_cities = pd.DataFrame({'Cities': Cities, 'Distance': Intracities_distance})
# print(Intra_cities)

# Plot the histogram for cities that are futhur than 71km
Intercities_score = [inverse_distance for cities, inverse_distance in list(sorted_dict.items())[87:]]
# Plot the histogram