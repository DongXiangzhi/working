import urllib.request
from bs4 import BeautifulSoup
import csv

webUrl = 'https://category.vip.com/search-1-0-1.html?q=3|30057&rp=30074|29741'


def getData(url):
    data = urllib.request.urlopen(url).read().decode('utf-8')
    return data


# print(getData(webUrl))


def Analysis_Content(info):
    soup = BeautifulSoup(info,'html.parser')
    # 接收图片的信息
    imageTags = soup.select('.goods-image-img')
    print(imageTags)
    # 接收价格信息
    priceTags = soup.select('.price')
    # 接收折扣信息
    discountTags = soup.select('.goods-discount')
    marketTags = soup.select('.goods-market-price')

    # goods列表用于保存原始数据，以便后面做更多扩展操作
    goods = []
    # 该列表中的数据需要按照存储表格中的数据格式进行整合
    csvdata = []
    # 对商品信息进行处理
    i=0
    for img in imageTags:
        goodsDic={}
        #对图片信息整合
        goodsDic['title']=img['alt']
        goodsDic['src']=img['src']
        #对价格信息整合
        priceTag=priceTags[i]
        price=''.join(priceTag)
        goodsDic['price']=price

        #对折扣信息整合
        discountTag=discountTags[i]
        discount=''.join(discountTag)
        goodsDic['discount']=discount

        #对市场信息整合
        marketTag=marketTags[i]
        marketTag.span.extract()
        market=''.join(marketTag)
        goodsDic['marketprice']=market

        #将整合好的信息加入列表
        goods.append(goodsDic)


        #对要写入表格的数据进行整合
        csvline=[]
        csvline.append(goodsDic['title'])
        csvline.append(goodsDic['price'])
        csvline.append(goodsDic['markettitle'])
        csvline.append(goodsDic['discount'])
        csvline.append(goodsDic['src'])
        csvdata.append(csvline)
        i+=1
    return goods,csvdata


print(Analysis_Content(getData(webUrl)))





