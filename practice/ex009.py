"""
给参数guess赋值，使得testcase永远通过。
"""
from random import randint, seed


seed(1)
guess = randint(1, 100)
seed(1)


if __name__ == '__main__':
    lucky_number = randint(1, 100)
    print(guess, lucky_number)
    
    
