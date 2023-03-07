###### THIS GAME IS ABOUT TO GUESSING A CUP WITH A BALL INSIDE

import random
import os


def clear_screen():
    return os.system("cls")


def shuffle_list(my_list):
    random.shuffle(my_list)
    return my_list


def player_guess():
    number = -1
    while number not in [0, 1, 2]:
        number = int(input("Type one number [0, 1, 2]: "))
    return number


def game_guess(my_list, guess):
    while True:
        if my_list[guess] == "O":
            clear_screen()
            print("CORRECT!!!")
            print(my_list)
            break
        else:
            clear_screen()
            print("WRONG!!!")
            print("Try again")
            guess = player_guess()


cup_list = [" ", "O", " "]
l = shuffle_list(cup_list)
guess = player_guess()
game_guess(l, guess)
