# -*- coding:utf-8 -*-
#获取哔哩哔哩视频封面
import bs4
import requests
import urllib

def getHttp(av):
    res = requests.get('https://www.bilibili.com/video/' + str(av) + '/')
    s = bs4.BeautifulSoup(res.text,'html.parser')
    e = s.find_all('body')[0].img.get('src')
    return 'http:' + e,e.split('.')[-1]

def saveImg(av,path):
    htaf = getHttp(av)
    f = open(path + r'\%s.%s'%(av,htaf[1]),'wb')
    f.write(urllib.urlopen(htaf[0]).read())
    f.close()

'''
av = 13860632
#saveImg(av,r'E://%s.png' %av)

print getHttp(av)
'''