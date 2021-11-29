import requests, execjs
from settings.settings import PRACTICE_ID

session = requests.session()
url = "https://www.python-spider.com/challenge/2"

cookies = {
    "sessionid":PRACTICE_ID

}

#res = session.get(url=url, cookies=cookies)

with open("two.js", "r")as f:
    js_text = f.read()
    compile = execjs.compile(js_text)
    cookie = compile.call("SDK")
    print(cookie.split(";")[0].replace("sign=", ""))
