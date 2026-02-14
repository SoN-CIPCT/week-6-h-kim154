#Conditional Lists
web_users = ['user1', 'user2','user3', 'user4', 'user5']
new_users = ['user1', 'user2', 'newuser3', 'newuser4', 'newuser5']

for user in new_users:
    if user in web_users:
        print("This user name is already in use. Please choose a different user name.")
    else:
        print("This user name is available.")


#Nested Dictionaries
cities = {}
cities['Tokyo'] = {'city':'Tokyo','country':'Japan', 'population':'33000000', 'fact':'Tokyo Disneyland opened in 1983'}
cities['Seoul'] = {'city':'Seoul','country':'South Korea', 'population':'96000000', 'fact':'one of the largest cities in the world'}
cities['London'] = {'city':'London','country':'the United Kingdom', 'population':'9900000', 'fact':'over 300 languages spoken by its diverse population'}

for city, info in cities.items():
    print('City:', city)
    print('Country:', info['country'])
    print('Population:', info['population'])
    print('Fact:', info['fact'])
    