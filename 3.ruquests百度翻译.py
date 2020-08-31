#!/user/bin/env python    
# -*- coding:utf-8 -*-
import requests
import json

if __name__ == "__main__":
    post_url = 'https://fanyi.baidu.com/sug'
    # 1.获取url(post)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
    }
    # 2.处理响应头（UA伪装
    word = input('input your word')
    data = {
        'kw': word
    }
    # 3.post请求处理（同get
    response = requests.post(url=post_url, data=data, headers=headers)
    # 4.发送请求
    dic_obj = response.json()
    filename = word + '.json'

    fp = open(filename, 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)
    # 5.持久化存储

    print('over!')
