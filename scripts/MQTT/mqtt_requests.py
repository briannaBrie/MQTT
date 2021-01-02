import json
import requests

headers = {'Content-Type':'applicaiton/json'}

response = requests.get('https://jsonplaceholder.typicode.com/posts/1',headers = headers)

if(reponse.status_code ==200):
    post = json.loads(response.content.decode('utf-8'))
    print(post['title'])
else:
    print("Error: "+str(response.status_code))