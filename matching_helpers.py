import json

AGE_THRESHOLD = 3

def get_age_score(users_age, age_low, age_high):
    '''
    Calculates the age related score
    Score of 1 if user is within the user's age preferences
    Score of 0.5 if within AGE_THRESHOLD of the user's age preferences
    0 otherwise
    '''
    if users_age >= age_low and users_age <= age_high:
        return 1
    elif users_age < age_low and users_age + AGE_THRESHOLD > age_low:
        return 0.5
    elif users_age > age_high and users_age - AGE_THRESHOLD < age_high:
        return 0.5
    else:
        return 0
    
def get_interests_score(users_interests, interests):
    '''
    Jaccard similarity for interest score
    '''
    intersect = len(set(users_interests).intersection(interests))
    union = len(set(users_interests).union(interests))
    return intersect/union


with open('cities_ranked.json', 'r') as json_file:
    distance_score = json.load(json_file)

distance_score_1 = dict(list(distance_score.items())[:87]) # The cut-off line is 80km, run Geolocation.py to see the box-plot and the distribution plot of distances beyond 80km.

distance_score_2 = dict(list(distance_score.items())[87:])

max_score = max(distance_score_2.values())
min_score = min(distance_score_2.values())

for key in distance_score_2:
    normalized_score = (distance_score_2[key] - min_score) / (max_score - min_score)
    distance_score_2[key] = normalized_score

def get_location_score(users_location, location):
    name_1 = f'{users_location} - {location}'
    name_2 = f'{location} - {users_location}'
    
    if users_location == location or name_1 in distance_score_1 or name_2 in distance_score_1:
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

        
