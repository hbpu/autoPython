import random
i

def hello():
    print('hello!你好!')

def hi(name):
    print(f'hi!{name}!')

def getAnswer(number):
    if number:
        return f'数字是{number}!'

def big_or_small():
    print(请输入一个数字：)
    number = input()
    r = random.randint(1, 100)
    answer = getAnswer(r)
    if number < answer:
        print(太小了)
    getAnswer()

if __name__ == '__main__':
    hello()
    hello()
    hi('yy')
    hi('hbpu')

