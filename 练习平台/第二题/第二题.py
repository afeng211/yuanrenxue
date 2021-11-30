import requests, execjs
from settings.settings import PRACTICE_ID

session = requests.session()
url = "https://www.python-spider.com/challenge/2"
# sign的加密
with open("two.js", "r")as f:
    js_text = f.read()
    compile = execjs.compile(js_text)
    cookie = compile.call("SDK")
cookies = {
    "sessionid":PRACTICE_ID,
    "sign": cookie.split(";")[0].replace("sign=", "")
}

res = session.get(url=url, cookies=cookies)

print(res.text)


