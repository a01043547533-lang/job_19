import requests

r = requests.get('https://search.incruit.com/list/search.asp?col=all&src=gsw*www&kw=%C6%C4%C0%CC%BD%E3', auth=('user', 'pass'))
print(r.status_code)



