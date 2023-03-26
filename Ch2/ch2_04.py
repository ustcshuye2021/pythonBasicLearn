a = b = c = 10
x = a + b + c + 12
print(x)

# 续行方法1
y = a + \
    b + \
    c + \
    12
print(y)

# 续行方法2
z = (a +  # 此处可以添加注释
     b +
     c +
     12)
print(z)
