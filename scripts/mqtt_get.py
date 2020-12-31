#you are tasked with retrieving and displaying a list of actors for movie Starship Troppers.
#send your Get request to a make a search by ID equal to 'tt0120201'(IMDB identifier of this moview)
#my key is: 57b0c05a
#his key is 2f810385

import json
import requests

headers = {"Content-Type": "application/json"}

response = requests.get('http://www.omdbapi.com/?={}&apikey = {}'.format('tt0120201', '57b0c05a'), headers = headers)

if(response.status_code==200):
    movie = json.loads(response.content.decode('utf-8'))
    print(movie['Actors'])
else:
    print('Error:'+str(response.status_code))
