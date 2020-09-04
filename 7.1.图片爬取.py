#!/user/bin/env python    
#-*- coding:utf-8 -*-
import requests
if __name__ == "__main__":
    url = 'https://pic.qiushibaike.com/system/pictures/12330/123308062/medium/NZZKWE4SZRMSL91G.jpg'
    photo = requests.get(url=url).content
    #content（）二进制   text（）文本  json（） 对象
    with open('./putian.jpg','wb',) as fp:
        fp.write(photo)