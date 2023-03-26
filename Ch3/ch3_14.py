# 从地球到月球约是384400千米，假设火箭的速度是一马赫
# 一马赫就是一倍声速，它的速度大约是每小时1225千米
# 设计一个程序计算需要多少天、多少小时才可抵达月球？
# 这个程序省略分钟数。

dist = 384400
speed = 1225
total_hours = dist // speed
days = total_hours // 24
hours = total_hours % 24
print(f"总共需要{days}天{hours}小时")
