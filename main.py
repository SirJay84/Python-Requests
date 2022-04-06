import requests
"""r = requests.get('https://pipedream.com/sources/dc_nvukKPR')"""

"""
r = requests.get('https://reqres.in/api/users/2')
print(r.text)
print(r.json())
json_data = r.json()
print(json_data['data']['last_name'])
"""
# r = requests.get('https://pipedream.com/sources/dc_nvukKPR?key1=value1&key2=value2')
'''
payload = {'first':'one','second':'two'}

r = requests.get('https://2a1f838fd36198aa414b5963af8abbf2.m.pipedream.net/', params=payload)
'''

'''
headers = {'my-token':'sndsfjjredllmdcdcdcddedilkkwwwdsclksddfdvdff'}

r = requests.get('https://2a1f838fd36198aa414b5963af8abbf2.m.pipedream.net/',headers=headers)
'''
# r = requests.post('https://2a1f838fd36198aa414b5963af8abbf2.m.pipedream.net/')

# r = requests.put('https://2a1f838fd36198aa414b5963af8abbf2.m.pipedream.net/')

# r = requests.delete('https://2a1f838fd36198aa414b5963af8abbf2.m.pipedream.net/')

# r = requests.patch('https://2a1f838fd36198aa414b5963af8abbf2.m.pipedream.net/')

'''
payload = {'name':'Jimmy', 'job':'Programmer'}
r = requests.post('https://reqres.in/api/users', json=payload)
print(r)
print(r.text)
print(r.json())
'''
'''
payload = {'name':'Jimmy','job':'Programmer','location':'Nairobi'}
r = requests.post('https://2a1f838fd36198aa414b5963af8abbf2.m.pipedream.net/', data=payload)
'''
'''
payload = {'name':'Jimmy','job':'Programmer','location':'Nairobi'}
r = requests.post('https://httpbin.org/post', data=payload)
print(r)
print(r.text)
print(r.json())
'''
'''
files = {'file': ('Agatha.jpg', open('Agatha.jpg','rb'), 'image/jpeg')}
r = requests.post('https://2a1f838fd36198aa414b5963af8abbf2.m.pipedream.net/', files=files)
print(r)
'''

'''
r = requests.get('https://httpbin.org//image/jpeg')
print(r.headers)
with open('Agatha.jpg','wb') as fd:
    for chunk in r.iter_content(chunk_size=500):
        fd.write(chunk)
'''

'''
r = requests.get('https://httpbin.org/status/501')
try:
    r.raise_for_status()
except requests.exceptions.HTTPError:
    print('ERROR! ERROR! ERROR!')
print(r)
'''
'''
try:
    r = requests.get('https://grgrgrhtjtjtbnbmmrtmbl.com')
except requests.exceptions.ConnectionError:
    print('CONNECTION ERROR!')
'''
'''
try:    
    r = requests.get('https://httpbin.org', timeout=0.001)
except requests.exceptions.ConnectTimeout:
    print('CONNECTION TIMEOUT!')
'''
'''
try:    
    r = requests.get('https://httpbin.org/delay/10', timeout=5)
except requests.exceptions.ReadTimeout:
    print('READ TIMEOUT!')
'''
'''
from requests.auth import HTTPBasicAuth
r = requests.get('https://httpbin.org/basic-auth/Jimmy/Jjmiwm18!', auth=HTTPBasicAuth('Jimmy','Jjmiwm18!'))
print(r)
'''

base_url = 'https://imdb-api.com/API/AdvancedSearch/k_nqlyktnc/?genres=action,adventure'

payload = {}

headers = {}

r = requests.request("GET", base_url, headers=headers, data = payload)
# print(r.text)
print(r.json())
# json_data = {'searchType':{'Movie'},'expression':{'inception 2010'}}
# print(json_data)
# json_data = r.json()
# print (json_data['results'][4])













