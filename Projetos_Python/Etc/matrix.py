import time
# import random


def rand(seed = None):
    if seed is None:
        seed = int(time.time() * 1000000) 
    while True:
        seed = (1103515245 * seed + 12345) % (2**31)
        yield seed / float(2**31)  

# def rand_lib():
#     return random.randint(0, 1)


print("\n"*100)
print("-------------------------QUAL LADO VOCE VAI ESCOLHER?-------------------------\n")
print(f"\33[{36}m1 - Pilula azul")
print(f"\033[0;31m2 - Pilula vermelha")
print(f"\033[1;37m")
num = int(input())

while True:
    if num == 1:        
        print(f"\33[{36}m{round(next(rand()))}", end = "")
        # print(f"\33[{36}m{rand_lib()}")

    elif num == 2:        
        print(f"\033[0;31m{round(next(rand()))}", end = "")
        # print(f"\033[0;31m{rand_lib()}")
    
    elif num not in [0, 1]:
        print("Você nao escolheu uma opçao disponível")
        break

