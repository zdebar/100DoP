import getpass
import requests

session = requests.Session()
session.get('http://httpbin.org/cookies/set/mipyt/best')

r = session.get('http://httpbin.org/cookies')
print(r.json())


session.headers.update({'x-test': 'true'})
r = session.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print(r.json())

