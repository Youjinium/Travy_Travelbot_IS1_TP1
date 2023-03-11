import re
import pandas as pd

# List Regex -> Responses
pattern_matching = [
    (r'I want to explore the continent (.+)[.]?', ['{0} is such a popular destination! Which country are you planning to visit?', 'Oops, looks like my travel map is missing {0}. Maybe it\'s a secret undiscovered continent? In any case, could you try another continent for now?'],'continent'),
    (r'I\'m planning to visit (.+)[.]?', ['{0} sounds amazing! How would you like to spend your vacation: exploring cities or nature?', 'Oops, looks like my travel map is missing {0}. Maybe it\'s a secret undiscovered country? In any case, could you try another destination for now?'], 'country'),
    (r'I want to explore (city|cities|nature)[.]?', ['{0} is an awesome choice. {1} is the perfect destination for you! Can you tell me the season you plan to visit in? (Spring/Summer/Autumn/Winter)'], 'city/nature'),
    (r'I plan to visit in (spring|summer|autumn|winter)[.]?', ['Sweet! {0} is a great time to go there! How many days do you want to stay there?', 'Uh-oh, looks like you\'re planning to time travel to a season that hasn\'t been discovered yet. Maybe you\'ll be the first to experience it! But for now, let\'s stick to the seasons that exist. Could you try another season for me?'], 'season'),
    (r'I would like to stay there for (\d+) days[.]?', ['Wow, you\'re gonna be there for {0} days! That sounds like a great adventure. What’s the budget you have in mind? (low/middle/high)'], 'duration'),
    (r'I have a (low|middle|high) budget in mind[.]?', ['I see that you have a {0} budget. Staying {1} is a great choice in that case. Your reservation has been confirmed.', 'Hmm, looks like your budget is a bit out of the ordinary. Perhaps you could try again with a low, middle, or high budget?'], 'budget'),
    (r'(.*)', ['I\'m having trouble understanding your input. Could you please try rephrasing it?'], 'default')
]


seasons = ['spring', 'summer', 'fall', 'winter']

budget_map = {
    'low': 'Hostel',
    'middle': 'Airbnb',
    'high': 'Hotel'
}


def valid_entry(csv, match, column):
    df = pd.read_csv(csv)
    return df[column].str.contains(match, case=False).any()

# Helper functions
def in_dataset(entity, value, travel_info):
    if entity == 'continent':
        travel_info['continent'] = value
        return valid_entry('dataset.csv', value, 'ContinentName')
    elif entity == 'country':
        travel_info['country'] = value
        return valid_entry('dataset.csv', value, 'CountryName')
    elif entity == 'season':
        if value in seasons:
            travel_info['season'] = value
            return True
        else: 
            return False
    else:
        travel_info[entity] = value
        return True


def chatbot_response(entity, is_true, responses, value):
    if entity == 'city/nature':
        if is_true:
            value = travel_info['country']
            # Get index of country entry in CSV
            df = pd.read_csv('dataset.csv')
            index = df[df["CountryName"].str.contains(value)].index[0]
            # Get entry of captial city corressponding to the country
            place = df.at[index, "CapitalName"]
            travel_info['place'] = place
            response = responses[0].format(value, place)
        else:
            response = responses[1].format(value)
    elif entity == 'budget':
        if is_true:
            budget = budget_map.get(str(value))
            response = responses[0].format(value, budget)
        else:
            response = responses[1].format(value)
    else:
        if is_true:
            response = responses[0].format(value)
        else:
            response = responses[1].format(value)
    return response

# User reponse to store in session
def init_travel_info():
    travel_info = {
        'continent': '',
        'country': '',
        'city/nature': '',
        'place': '',
        'season': '',
        'duration': '',
        'budget': ''
    }
    return travel_info

# Function to check if travel_info hashmap is all filled
def all_slots_filled(travel_info):
    for slot in travel_info.values():
        if not slot:
            return False
    return True


# Chatbot
def travy_chatbot(msg, travel_info):
    for pattern, responses, entity in pattern_matching:
        match = re.search(pattern, msg, re.IGNORECASE)
        if match: 
            value = match.group(1)
            is_true = in_dataset(entity, value, travel_info)
            return chatbot_response(entity, is_true, responses, value)


# Main
print('##########################################################################')
print('                         Travy the Travel Chatbot                         ')
print('##########################################################################\n')
travel_info = init_travel_info()
print('Hello, I am Travy! I am a travel bot. Which continent do you want to explore?')
while True:
    user_msg = input('User: ')
    print(travy_chatbot(user_msg, travel_info))
    # Check if all slots are filled
    if all_slots_filled(travel_info):
        # Create a txt file where the user responses are stored
        with open('travel_info.txt', 'w') as f:
            for key, value in travel_info.items():
                f.write(f'{key}: {value}\n')







'''
For presentation

Objectives
Methododlogies
INteresting stuff
'''