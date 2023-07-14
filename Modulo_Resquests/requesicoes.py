import requests

response = requests.get('https://www.walissonsilva.com/')

print('Status Code:' , response.status_code)

print('header')
print (response.headers)

print('\nContent')
print(response.content)