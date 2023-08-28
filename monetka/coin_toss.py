from numpy import random


def coin_toss():
    coin = ['orel', 'reshka', 'rebro']
    probability = [0.4, 0.4, 0.2]
    result = random.choice(coin, p=probability)
    
    return result


if __name__ == '__main__':

    # на 100 бросков ~3 ребра
    for i in range(0, 100):
        print(coin_toss())
