# 通过身高体重计算人体的BMI指数
# 判断其体重是否正常
height = input("请输入身高(cm):")
weight = input("请输入体重(kg):")
bmi = int(weight) / ((float(height) / 100) ** 2)
if 18.5 <= bmi < 24:
    print("体重正常")
else:
    print("体重不正常")

