# round()函数 官网学习：https://docs.python.org/3/
# 思考：print(f"取整后的数字是：{round(int(str))}")这是一个什么错误？

print("请输入一个小数：")
string = input()
num = float(string)
try:
    print(f"取整后的数字是{round(num)}")
except TypeError as err:
    print(err)
