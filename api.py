#9fb8cd70cb34cab8e83690473133f51943b5c93f


#from urllib.request import urlopen
#import json
#url = 'https://api.fullcontact.com/v2/person.json?apikey=68d0e9907bc7182b&email=rohit.yadav848%40yahoo.com'
#Data = urllib.request.Request(url)
#urlData = urllib.request.urlopen(Data)
#response = urlopen(url).read().decode('utf8')
#obj = json.loads(response)


import requests
import json

url = 'https://api.fullcontact.com/v2/person.json?apikey=3558403aafc12f64&email=markcuban%40dallasmavs.com'
print("Fetching url..")
response = requests.get(url, verify=True)
#loaded_json = json.loads(urlData)
if response.status_code != 200:
	print('Status:', response.status_code, 'Problem with the request. Exiting.')
	exit()
data = response.json()