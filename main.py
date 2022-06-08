###
#
# File: main.py
# Version 1.0.0
# Date 14:28 25.03.2022
# Copyright (c) 2022 S. A. Ditlefsen
# License: http://opensource.org/licenses/gpl-license.php GNU Public License
#
###

import time

from coupon import Coupon
from drawer import Drawer


class Main:
    __coupon = Coupon()
    __drawer = Drawer()
    __wallet = 0
    __coupon_price = 60
    __drawings_counter = 0

    def __init__(self):

        # Welcome
        print("Welcome to Lottosim\n")

        print("Lotto is a game where", end=" ")
        print("you purchase coupon ")
        print("with 10 rows, each consisting", end=" ")
        print("of 7 numbers.")
        print(f"Each coupon costs {self.__coupon_price}.\n ")

        print("Prices are given for:")
        print(" * 7 main numbers - 14 039 045")
        print(" * 6 main + 1 additional number - 65 105")
        print(" * 6 main numbers - 4315")
        print(" * 5 main numbers - 110")
        print(" * 4 main numbers - 50")

        # Ask how many drawings
        print("")
        print("How many drawings do you want?")
        print("Enter a number between 1 and \"until_winner\"")
        drawings: str = input()
        print("Lets do this!")

        if drawings == "until_winner":
            # endless drawings
            stop = 0
            while (stop < 1):
                is_winner = self.draw()
                if (is_winner):
                    stop = 1
                    break
        else:
            # number of drawings
            number_of_drawings = int(drawings)
            for z in range(number_of_drawings):
                is_winner = self.draw()
                if (is_winner):
                    break

    def draw(self):
        # Drawings counter
        self.__drawings_counter += 1

        # Header
        years_double = self.__drawings_counter / 52
        years_int = int(years_double)
        print("")
        print(f"~~~~~~~~ Drawing {self.__drawings_counter}", end="")
        print(f" - Year {years_int} ", end="")
        print("~~~~~~~~\n")

        # Update wallet with price
        self.__wallet = self.__wallet - self.__coupon_price

        self.__drawer.draw_main_numbers()
        self.__drawer.draw_sub_number()
        self.__drawer.print_numbers()
        my_results: list = self.__drawer.check_if_won(self.__coupon)

        my_gain = self.__drawer.get_gain()

        # Print my results
        is_winner = False
        if len(my_results) > 0:
            for result in my_results:
                if result == "7+0":
                    print({result})
                    print("~ ~ ~ ~ ~ W I N N E R ~ ~ ~ ~ ~")
                    is_winner = True
                elif result == "6+1":
                    print({result})
                    print("~ ~ ~ ~ ~ A L M O S T. W I N N E R ~ ~ ~ ~ ~")
                elif result == "6+0":
                    print({result})
                elif result == "5+0" or result == "5+1":
                    print({result})
                elif result == "4+0" or result == "4+1":
                    print({result})

            # Update wallet with result
            self.__wallet = self.__wallet + my_gain

            # Print gain
            print(f"Gain: {my_gain: }")
            print(f"Wallet: {self.__wallet: }")

        # Sleep before return
        time.sleep(1)

        return is_winner


Main()
