# 格式化输出的调控
x = 100
print("x=/%6d/" % x)
y = 10.5
print("y=/%6.2f/" % y)
s = "Deep"
print("s=/%6s/" % s)
print("以下是保留格数空间不足的实例")
print("x=/%2d/" % x)
print("y=/%3.2f/" % y)
print("s=/%2s/" % s)
