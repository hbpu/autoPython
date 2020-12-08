import random, sys

print("口算100道题天天练")

for i in range(100):
    num01 = random.randint(1, 100)
    num02 = random.randint(1, 100)
    sum01 = num01 + num02
    print(f"{num01}+{num02}=")
    res = input()
    if res == "exit":
        sys.exit()
    try:
        if int(res) == num01 + num02:
            print("答对了！")
        if int(res) != num01 + num02:
            print(f"加油，答错了，正确答案是{sum01}")
    except:
        continue