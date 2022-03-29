import json 
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

