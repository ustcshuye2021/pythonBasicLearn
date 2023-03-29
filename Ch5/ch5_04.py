# 判断输入整数的奇偶性
print("奇数偶数的判断")
num = int(input("请输入任意整数值："))
rem = num % 2
if rem == 0:
    print("%d 是奇数" % num)
else:
    print("%d 是偶数" % num)
