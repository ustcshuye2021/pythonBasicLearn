# 输入华氏温度，输出摄氏温度
f = input("请输入华氏温度：")
c = (float(f) - 32) * 5 / 9
print("华氏 %s℉ 等于摄氏 %4.1f℃" % (f, c))
