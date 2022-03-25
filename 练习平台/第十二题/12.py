# -*- coding : utf-8-*-
# coding:unicode_escape
# /* chrome、firefox */
import requests
from fontTools.ttLib import TTFont

# 读取文件字体
font = TTFont("aiding.woff")
# 生成一个xml文件查看映射关系
font.saveXML("aiding.xml")

# 创建一个空字典以储存字体文件中字体跟编码的映射关系
font_dict = {}

# getBestCmap是返回cmap中code 跟name的映射，返回为字典格式，遍历字典的话要调用items的方法，
# 变为可迭代对象，运行item结果为：
# dict_items([(58441, 'unie449'), (58445, 'unie44d'), (58456, 'unie458'), (61002, 'uniee4a'), (61654, 'unif0d6'), (61743, 'unif12f'), (62101, 'unif295'), (62325, 'unif375'), (63250, 'unif712'), (63500, 'unif80c')])
# 把字典中的键跟值组成一对对元组放在一个列表中

# 遍历字典提取映射关系储存到新字典中
for key,value in font.getBestCmap().items():
    # key为cmap中code的值，value为cmap中name的值
    # 十六进制默认为转位十进制所以用hex（）方法把他转回十六进制

    font_dict[hex(key)] = font.getGlyphID(value)

url = "https://www.python-spider.com/api/challenge12"

data = {
    "page": 1
}
res = requests.post(url=url,data=data)
# 取出网页上加密后的数字
for value in res.json()["data"]:
    str = value["value"]
    # 把字符串替换成十六进制格式的再切割
    print(str.replace("&#","0").split())

print(font_dict)




