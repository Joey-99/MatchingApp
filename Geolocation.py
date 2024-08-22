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
#print(sorted_dict)
#write_dict_to_json(sorted_dict, 'cities.json')

import matplotlib.pyplot as plt

# Divide the sorted_dict into five parts evenly
n = len(sorted_dict)
print(f"the numbers of scores are {n}")
part_size = n // 5
print(f"the size of each quantile is {part_size}")
parts = [list(sorted_dict.items())[i:i+part_size] for i in range(0, n, part_size)]

# Create a list to store the box plot data
box_plot_data = []

# Iterate over each part and extract the inverse distances
for part in parts:
    distances = [1/inverse_distance for _, inverse_distance in part]
    box_plot_data.append(distances)

# # Plot the box plots
# plt.boxplot(box_plot_data)
# plt.xlabel('Part')
# plt.ylabel('Inverse Distance')
# plt.title('Box Plot of Inverse Distances')
# plt.show()

#print(f"The distance of the cutoffline in {list(sorted_dict.items())[10][0]} is {1/list(sorted_dict.items())[10][1]} km.")

Intracities_distance = [1/inverse_distance for cities, inverse_distance in list(sorted_dict.items())[80:87]]
Cities = [cities for cities, inverse_distance in list(sorted_dict.items())[80:87]]
Intra_cities = pd.DataFrame({'Cities': Cities, 'Distance': Intracities_distance})
print(Intra_cities)

Intercities_score = [inverse_distance for cities, inverse_distance in list(sorted_dict.items())[87:]]
# Plot the histogram
plt.hist(Intercities_score, bins=10)
plt.xlabel('Distance')
plt.ylabel('Frequency')
plt.title('Distance Distribution')
plt.show()