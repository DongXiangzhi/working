# Spider_Videos
import urllib.request
from bs4 import BeautifulSoup

webUrl = 'http://tieba.baidu.com/p/5657604550'

'''
<video style="width: 565px; height: 317.8125px; background: #000;" src="http://tb-video.bdstatic.com/tieba-smallvideo-transcode/22420149_e5b18737b23ab9cdcd8913bb4a317110_1.mp4" autoplay="true" controls="controls" data-md5="e5b18737b23ab9cdcd8913bb4a317110" data-threadid="5657604550"></video>
'''

def getData(url):
    data = urllib.request.urlopen(url).read()
    file = open("data/003.html", "wb")
    file.write(c)
    return data


# print(getData(webUrl))

def getVideos(info):
    # 定义一个soup对象，用于记录页面信息
    # 此时整个页面里的内容全部存在soup里

    soup = BeautifulSoup(info,"lxml",from_encoding="utf-8")
    
    allVideos = soup.find_all('div',attrs={"class":"video"})
    print(str(len(allVideos)) + "个视频找到了！")


print(getVideos(getData(webUrl)))