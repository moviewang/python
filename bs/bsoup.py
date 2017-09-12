import bs4
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3" target="_blank">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
print('html:', html)
soup = BeautifulSoup(html)
#格式化输出内容
print(soup.prettify())

'''四大数据类型 tag, navigaleString,BeautifulSoup,comment '''

title = "<title>The Dormouse's story</title>"
tagsoup = BeautifulSoup(title)
print('title: %s' % tagsoup.title)
print('p: %s' % soup.p)
print('a: %s' % soup.x)
print('a: %s' % type(soup.p))
print('a: %s' % soup.name)
print('a: %s' % soup.attrs)
print('attrs: %s' % soup.p.attrs)
print('name: %s' % soup.p.name)
print('attrs name: %s' % soup.p.attrs['class'])
print('attrs name: %s' % soup.p['class'])
soup.p['class'] = 'new class'
print('attrs name: %s' % soup.p['class'])
del soup.p['class']
print('attrs name: %s' % soup.p)
print('p.string:', soup.p.string, type(soup.p.string))
#beautifulsoup is special tag
print(soup.name)
print(soup.attrs)
print(type(soup))

comment = """<a class="sister" href="http://example.com/elsie" id="link1">
<!-- Elsie -->hello</a>
Elsie 
<class 'bs4.element.Comment'>"""
#加上lxml后注释的内容不显示
soup_comment = BeautifulSoup(comment, 'lxml')
print('comment:', soup_comment.a.prettify())
print(soup_comment.a.string)
print(soup.a.string)
print(soup.find_all('a'))

# if type(soup_comment.a.string) == bs4.elem

url = ' http://www.x23us.com/class/1_'
print(url[url.rfind('/') + 1 : url.rfind('_')])

