#!/user/bin/env python    
# -*- coding:utf-8 -*-
import requests
import re

if __name__ == "__main__":
    url = 'https://www.qiushibaike.com/imgrank/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
    }
    page_text = requests.get(url=url, headers=headers).text
    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?<div>'
    img_src_list = re.findall(ex, page_text, re.S)
    print(img_src_list)
