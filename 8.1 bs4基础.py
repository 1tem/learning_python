#!/user/bin/env python    
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
# 导入beautifulsoup
import lxml

# 解析器
if __name__ == "__main__":
    fp = open('./123.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp, 'lxml')
    # print(soup)
    # print(soup.div)
        # print(soup.tagname) 提取html中第一个该标签名所包含的内容
    # print(soup.find('div'))
        # print(soup.find('tagname'))等同于print(soup.tagname)
    # print(soup.find('div', class_='hzbscbox'))
        # print(soup.find('tagname',class_/id/attr='hzbscbox')) 起定位属性作用
        # print(soup.find_all('tagname')) 提取html中所有该标签名所包含的内容
    # print(soup.select('.hzbscbox'))
        # select('某种选择器(id，class，标签==)')，其中id前需要加#，类前需要加. ，标签什么都不加
    # print(soup.select('.hzbscbox > div > div > div > span')[0])
        # 层级选择 >表示层级递进关系（一层一层深入
    # print(soup.select('.hzbscbox > div > div span')[0])
        # 层级选择 空格表示层级递进关系（多个层级深入
    # print(soup.select('.hzbscbox > div > div span')[0].text)
        # .text/.string/.get_text() 提取被定位后的文本
    # print(soup.find('div', class_='hzbscbox').string)
        # text/get_text可以获取该标签层级内所有文本内容
        # string只能获得该定位标签内内容
    # print(soup.select('.hzbbtm a')[0]['href'])
        # 提取某标签中的属性值