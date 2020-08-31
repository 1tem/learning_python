#!/user/bin/env python    
# -*- coding:utf-8 -*-

# UA：User-Agent(请求载体身份标识)
# UA检测：网站会检测响应请求的UA，如果UA为浏览器，说明该请求为正常请求，如果UA标识不是基于某款浏览器的，则会怀疑该请求
# 为爬虫，服务器端会限制或禁止该请求

# UA伪装：让爬虫对应的UA伪装成某一款浏览器
import requests

if __name__ == "__main__":
    # UA伪装：将对应的User-Agent封装在一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
    }
    url = 'https://www.sogou.com/web?'
    # 1.获取url,并处理其中的参数到字典中
    word = input('请输入一个关键词或句子')
    param = {
        'query': word
    }
    # 本url中的参数为query
    # 2.对指定的url发起的请求对应的url是携带了参数的，并且在请求过程中处理了参数
    response = requests.get(url=url, params=param, headers=headers)
    # 3.获取响应数据
    page_text = response.text
    fileName = word + '.html'

    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    # 4.持久化存储
    print(fileName, '保存成功！')
