import csv
#打开一个csv表格文件（如果没有则创建），打开方式是只写

csvFile=open('test.csv','w')

#创建一个写的对象，用于对csv文件写入
writer=csv.writer(csvFile,dialect=("excel"))

#写一行内容
writer.writerow(['name','age','children'])

data=[('东东','40','3'),
     ('东东2','30','1'),
     ('东东3','20','1')]

writer.writerows(data)
csvFile.close()
#创键一个读文件句柄
rf=open('test.csv','r')
#创建度对象
reader=csv.reader(rf)
print(reader)
for row in reader:
    print(row)
    pass
