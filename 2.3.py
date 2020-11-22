while True:
    print("你的用户名是：")
    name = input()
    if name != "Andy":
        continue
    print("你好，你的密码是：")
    password = input()
    if password == "andy":
        break
print("欢迎您！")