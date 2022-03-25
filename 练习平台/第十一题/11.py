import requests

url = "https://www.python-spider.com/challenge/11"
data = {

}

res = requests.get(url=url)

print(res.text)