# 使用divmod()函数重新设计ch3_14.py

dist = 384400
speed = 1225
total_hours = dist // speed
days, hours = divmod(total_hours, 24)
print(f"总共需要{days}天{hours}小时")
