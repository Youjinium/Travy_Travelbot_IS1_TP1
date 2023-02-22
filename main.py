import re

from sympy import true

# List Regex -> Responses
pattern_matching = [
    (r'I want to explore the continent (.+)[.]?', ['{0} is such a popular destination! Which country are you planning to visit?', 'Oops, looks like my travel map is missing {0}. Maybe it\'s a secret undiscovered continent? In any case, could you try another continent for now?'],'continent'),
    (r'I\'m planning to visit (.+)[.]?', ['{0} sounds amazing! How would you like to spend your vacation: exploring cities or nature?', 'Oops, looks like my travel map is missing {0}. Maybe it\'s a secret undiscovered country? In any case, could you try another destination for now?'], 'country'),
    (r'I want to explore (city|cities|nature)[.]?', ['{0} is an awesome choice. Paris is the perfect destination for you! Can you tell me the season you plan to visit in? (Spring/Summer/Autumn/Winter)'], 'city/nature'),
    (r'I plan to visit in (spring|summer|autumn|winter)[.]?', ['Sweet! {0} is a great time to go there! How many days do you want to stay there?', 'Uh-oh, looks like you\'re planning to time travel to a season that hasn\'t been discovered yet. Maybe you\'ll be the first to experience it! But for now, let\'s stick to the seasons that exist. Could you try another season for me?'], 'season'),
    (r'I would like to stay there for (\d+) days[.]?', ['Wow, you\'re gonna be there for {0} days! That sounds like a great adventure. What’s the budget you have in mind? (low/middle/high)'], 'days'),
    (r'I have a (low|middle|high) budget in mind[.]?', ['I see that you have a {0} budget. Staying {1} is a great choice in that case. Your reservation has been confirmed.'], 'accomodation'),
    (r'(.*)', ['I\'m having trouble understanding your input. Could you please try rephrasing it?'], 'default')
]



valid_continents = ['Africa', 'Antarctica', 'Asia', 'Australia', 'Europe', 'North America', 'South America']
valid_countries = ['France', 'Italy', 'Spain', 'Germany', 'United Kingdom', 'Greece']
cities = ['Paris', 'Barcelona', 'Rome', 'Amsterdam', 'Vienna', 'Berlin', 'Prague', 'Dublin', 'Athens']
seasons = ['spring', 'summer', 'fall', 'winter']


# Helper functions
def in_list(entity):
    if entity == 'continent':
        return valid_continents
    elif entity == 'country':
        return valid_countries
    elif entity == 'season':
        return seasons
    else:
        return None


def value_is_valid(value, list):
    if list == None:
        return True
    else:           
        if value in list:
            return True
        else:
            return False
  


def chatbot_response(is_true, responses, value):
    if is_true:
        response = responses[0].format(value)
    else:
        response = responses[1].format(value)
    return response

# Chatbot
def travy_chatbot(msg):
    for pattern, responses, entity in pattern_matching:
        match = re.search(pattern, msg, re.IGNORECASE)
        if match: 
            value = match.group(1)
            is_true = value_is_valid(value, in_list(entity))
            return chatbot_response(is_true, responses, value)


# Main
print('##########################################################################')
print('                         Travy the Travel Chatbot                         ')
print('##########################################################################\n')

print('Hello, I am Travy! I am a travel bot. Which continent do you want to explore?')
while True:
    user_msg = input('User: ')
    print(travy_chatbot(user_msg))





patterns = [
    (r'Hello|Hi|Hey', ['Hello! This is Travy. I’m a travel bot. Which continent are you planning to go next?']),
    (r'I\'m planning a trip to ([a-zA-Z]+)', ['{0} is such a popular destination! Which country are you thinking about?']),
    (r'I want to go to ([a-zA-Z]+)', ['{0} has a lot to offer! Do you prefer to visit a city or to explore a nature site?']),
    (r'I prefer to visit a city', ['Great choice! What kind of city are you interested in?']),
    (r'I prefer to explore a nature site', ['Sounds like a great idea! What kind of nature site are you interested in?']),
    (r'(.*)', ["I'm sorry, I don't understand. Can you please rephrase that?"])
]