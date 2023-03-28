# 分别输入中文和英文的姓氏以及名字，将名字组合然后输出问候语
clastname = input("请输入中文姓氏：")
cfirstname = input("请输入中文名字：")
cfullname = clastname + cfirstname
print("%s 欢迎使用本系统" % cfullname)
lastname = input("Please Input Last Name: ")
firstname = input("Please Input First Name: ")
fullname = firstname + " " + lastname
print("%s Welcome to SSE System" % fullname)
