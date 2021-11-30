import requests

url = "https://www.python-spider.com/api/challenge3"

res = requests.get(url=url)

print(res.text)