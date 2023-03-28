# 基本数据输入与运算
print("欢迎使用成绩输入系统")
name = input("请输入姓名：")
engh = input("请输入英语成绩：")
math = input("请输入数学成绩：")
total = int(engh) + int(math)
print("%s 你的总分是 %d" % (name, total))
