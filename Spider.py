import urllib.request  # 导入抓取网络数据模块
import re  # 导入正则表达式模块
import os


def get_data(url):
    # urlopen:创建一个表示远程url的类文件对象，然后像本地文件一样操作这个类文件对象
    # RETURN 会返回一个类文件对象
    # read()  ,readline(),readlines(),fileno(),close()
    #     f=urllib.urlopen(url)
    #     data=f.read()
    #     f.close()

    data = urllib.request.urlopen(url).read().decode('utf-8')
    return data


# web_url='https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_2404958430258319355%22%7D&n_type=0&p_from=1'
# print(get_data(web_url))

def crawler_images(info):
    # 通过正则表达式匹配目标图片的网址
    r = r'src="(.+?\.jpg)"'
    # 创建一个正则对象
    pat = re.compile(r)
    images = re.findall(pat, info)
    print(str(len(images)) + '图片被找到了！')
    # 循环批量下载找到的图片
    os.system('mkdir MyCrawlImages')
    i = 0
    for imgUrl in images:

        match=re.search("http://",str(imgUrl))
        if match:
            print(imgUrl)
            urllib.request.urlretrieve(imgUrl,'MyCrawlImages/%s. jpg'% i)
            i+=1

web_url = 'http://www.ucas.ac.cn/'
print(crawler_images(get_data(web_url)))
