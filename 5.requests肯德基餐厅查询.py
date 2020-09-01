#!/user/bin/env python    
# -*- coding:utf-8 -*-
import requests

if __name__ == "__main__":
    post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?'
    plance = input('请输入要查询的地点')
    page = input('请输入要查询的页数')
    param = {
        'op': 'keyword',
        'cname': '',
        'pid': '',
        'keyword': plance,
        'pageIndex': page,
        'pageSize': '10',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
    }
    response = requests.post(url=post_url, params=param, headers=headers)
    page_text = response.text
    with open('./kfc.json', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('over')
