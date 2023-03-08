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


# Initialize the travel_info dictionary
travel_info = init_travel_info()



def all_slots_filled(travel_info):
    for slot in travel_info.values():
        if not slot:
            return False
    return True


# Check if all slots are filled
if all_slots_filled(travel_info):
    print('All slots are filled!')
else:
    print('Some slots are still empty.')
