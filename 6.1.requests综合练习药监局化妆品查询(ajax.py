#!/user/bin/env python    
#-*- coding:utf-8 -*-
import requests
if __name__ == "__main__":
    url = 'http://scxk.nmpa.gov.cn:81/xk/'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
    }
    data_text = requests.get(url=url,headers=headers).text
    with open('./huazhuangping.html','w',encoding='utf-8') as fp:
        fp.write(data_text)
