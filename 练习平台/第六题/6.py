import requests
# 骚操作，只要用个session保持就可以搞定，不然的话第51页会有脏数据
url = "https://www.python-spider.com/api/challenge6"

session = requests.session()
num = 0
for i in range(1,101):
    data = {
        "page" : i
    }
    res = session.post(url, data=data)
    for value in res.json()["data"]:
        num += int(value["value"])
    print(f"已请求{i}页")
print(num)
