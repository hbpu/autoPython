import random
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')

def hello():
    print('hello!你好!')

def hi(name):
    print(f'hi!{name}!')

def getAnswer(number):
    if number:
        return f'数字是{number}!'

def big_or_small():
    print('请输入一个数字：')
    number = input()
    r = random.randint(1, 100)
    answer = getAnswer(r)
    if int(number) < int(r):
        logging.debug(number)
        logging.debug(answer)
        print('太小了')
    

if __name__ == '__main__':
    hello()
    hello()
    hi('yy')
    hi('hbpu')
    big_or_small()

