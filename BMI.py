# BMI.py
# 低于18.5
# 正常：18.5-23.99
# 过重：24-27
# 肥胖：28-32
# 非常肥胖：高于32


print('请输入你的身高（厘米）\n')
height=float(input())
print('请输入你的体重（公斤）\n')
weight=float(input())

bmi=weight/(height/100*height/100)
print('bmi='+str(bmi))

if (bmi>=18.5 and bmi<23.99):
    print('正常！')
elif (bmi>=23.99 and bmi<27):
    print('偏重了！')
elif (bmi>=28 and bmi<32):
    print('国胖')
elif (bmi<18.5):
    print('偏瘦')
elif (bmi>=32):
    print('太重了！')
a=2
b=3
if (a>b): print(a)
else: print(b)

# 正确性
# 清晰性
# 重用性
# 扩展性
# 效率
# 可移植性





