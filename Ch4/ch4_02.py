# 重写ch4_01.py，使得两个数据在同行输出（用tab的距离隔开）
# print的end参数
num1 = 222
num2 = 333
num3 = num1 + num2
print("这是数值相加", num3, end="\t")
str1 = str(num1) + str(num2)
print("强制转换为字符串相加", str1, sep=" $$$ ")