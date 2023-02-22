import re

# List Regex -> Responses
pattern_matching = [(r'I want to explore the continent (.+)[.]?', ['{0} is such a popular destination! Which country are you thinking about?', 'Oops, looks like my travel map is missing {0}. Maybe it\'s a secret undiscovered continent? In any case, could you try another destination for now?'],'continent')]



valid_continents = ['Africa', 'Antarctica', 'Asia', 'Australia', 'Europe', 'North America', 'South America']

# Helper functions
def value_is_valid(value, entity):
    if entity == 'continent':
        if value in valid_continents:
            if value in valid_continents:
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
            is_true = value_is_valid(value, entity)
            return chatbot_response(is_true, responses, value)


# Main
print('##########################################################################')
print('Hello, I am Travy! I am a travel bot. What continent do you want to explore?')
print('##########################################################################')
print()
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