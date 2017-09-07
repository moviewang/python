#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
import urllib.request
import re
import json

#返回byte
def download_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    return response.read()

def get_img(html):
    regex = r'https://[\S]*\.jpg'
    pattern = re.compile(regex)
    images = re.findall(pattern, repr(html))
    print('images:', images)
    num = 1
    for img in images:
        print('img url:', img)
        image = download_page(img)
        with open('d:/pic/douban/%s.png' % num, 'wb') as fp:
            fp.write(image)
            num += 1
            print('download %s pic' % num)
def  get_img2(html):
    #byte 转成字符串
    html_str = html.decode('utf-8')
    dict = json.loads(html_str)
    print('dict:', dict['subjects'])
    num = 0
    for subject in dict['subjects']:
        print('img url:', subject['cover'])
        image = download_page(subject['cover'])
        with open('d:/pic/douban/%s.png' % subject['title'], 'wb') as fp:
            fp.write(image)
            num += 1
            print('download %s pic' % num)


for i in range(0,100,20):
    print('page:', i)
    url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start='+ repr(i)
    html = download_page(url)
    # print('html:', type(html), html.decode('utf-8'))
    #
    # html_str = html.decode('utf-8')
    # dict = json.loads(html_str)
    # print('dict:', dict['subjects'])
    #
    # for subject in dict['subjects']:
    #     print(subject['cover'])

    get_img2(html)

