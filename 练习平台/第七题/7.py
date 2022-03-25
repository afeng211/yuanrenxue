import requests
# 这题得请求两个地址，第一个拿到时间再请求第二个才会给数据，目前还不知道原理，等我会了之后再看看研究下
requrl = "https://www.python-spider.com/cityjson"
url = "https://www.python-spider.com/api/challenge7"

session = requests.session()
num = 0

for page in range(1,101):
    data = {
        "page": page
    }
    session.post(requrl)
    res = session.post(url,data=data)
    for i in res.json()["data"]:
        num += int(i["value"])
    print(f"第{page}页")
    print(num)
print(num)
