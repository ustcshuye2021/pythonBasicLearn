# 输出绝对值
print("输出绝对值")
num = input("请输入任意整数值：")
x = int(num)
if int(x) < 0:
    x = abs(x)
print("绝对值是 %d" % int(x))
