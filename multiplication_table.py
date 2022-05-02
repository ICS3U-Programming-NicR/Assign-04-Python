#!/usr/bin/env python3

# Created By: Nicolas Riscalas

# Date: 26-04-2022

# creates a multiplication system

import colorama
from colorama import Fore, Back, Style


def main():
    while True:
        repeat_num_str = input(
            Fore.CYAN
            + "Enter the amout of times you want to repeat the multiplication table: "
        )
        user_num_str = input(Fore.CYAN + "Enter the number you want to multiply: ")
        try:
            repeat_num = int(repeat_num_str)
            user_num = int(user_num_str)
            counter = 0
            for counter in range(repeat_num + 1):
                print(
                    Fore.GREEN
                    + "{} * {} = {}".format(user_num, counter, user_num * counter)
                )
        except:
            print("you have to enter a number not a string")
        input(Fore.RED + "press <enter> if you want to restart")
        continue


if __name__ == "__main__":
    main()
