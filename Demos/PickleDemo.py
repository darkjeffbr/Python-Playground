import pickle

website = {
    'title': 'Techbeamers',
    'site_link' : '/',
    'site_type' : 'technology blog',
    'owner': 'Python Serialization tutorial',
    'established_date': 'Nov2017'
}

print('Before Serialization')
print(website)

with open('website.pickle', 'wb') as f:
    print('Serializing / Marshaling')
    pickle.dump(website,f)

with open('website.pickle', 'rb') as f:
    print('Deserializing / Unmarshaling')
    data = pickle.load(f)
    print(data)
