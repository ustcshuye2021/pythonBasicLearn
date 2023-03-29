# 测试某一年是否是闰年
print("判断输入年份是否闰年")
year = int(input("请输入年份："))
rem4 = year % 4
rem100 = year % 100
rem400 = year % 400
if rem4 == 0:
    if rem100 != 0 or rem400 == 0:
        print("%d 是闰年" % year)
    else:
        print("%d 不是闰年" % year)
else:
    print("%d 不是闰年" % year)
    