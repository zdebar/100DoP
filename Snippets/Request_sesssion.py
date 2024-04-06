session = requests.Session()
session.get('http://httpbin.org/cookies/set/mipyt/best')
<Response [200]>
r = session.get('http://httpbin.org/cookies')
r.json()
{'cookies': {'mipyt': 'best'}}
session.headers.update({'x-test': 'true'})
r = session.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
r.json()
{'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'close', 'Cookie': 'mipyt=best', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.19.1', 'X-Test': 'true', 'X-Test2': 'true'}}