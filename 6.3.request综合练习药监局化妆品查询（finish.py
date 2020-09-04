#!/user/bin/env python
# -*- coding:utf-8 -*-
import requests
import json

if __name__ == "__main__":
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
    }
    all_data_list = []  # 存储所有企业数据
    ids_list = []  # 存储企业id
    for page in range(1,6):
        page = str(page)
        data = {
            'on': 'true',
            'page': '1',
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': '',
        }
        dic_obj = requests.post(url=url, params=data, headers=headers).json()
        for dic in dic_obj['list']:
            ids_list.append(dic['ID'])
    #print(ids_list)
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in ids_list:
        data = {
            'id': id
        }
        detail_json = requests.post(url=post_url, headers=headers, data=data).json()
        #print(detail_json)
        all_data_list.append(detail_json)
    fp = open('./huazhuangping.json','w',encoding='utf-8')
    json.dump(all_data_list,fp=fp,ensure_ascii=False)