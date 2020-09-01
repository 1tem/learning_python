#!/user/bin/env python    
# -*- coding:utf-8 -*-
import json
import requests

if __name__ == "__main__":
    get_url = 'https://movie.douban.com/j/chart/top_list?'
    # 1.获取url（get）
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '20',
    }
    # 2.封装参数
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
    }
    # 3.伪装UA
    response = requests.get(url=get_url, params=param, headers=headers)
    # 4.获取响应

    list_data = response.json()
    fp = open('./douban.json', 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)
    # 5.持久化存储
    print('over!')
