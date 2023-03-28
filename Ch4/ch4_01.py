# print的sep参数 - 分隔符
num1 = 222
num2 = 333
num3 = num1 + num2
print("这是数值相加", num3)
str1 = str(num1) + str(num2)
print("强制转换为字符串相加", str1, sep=" $$$ ")
