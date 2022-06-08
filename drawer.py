###
#
# File: drawer.py
# Version 1.0.0
# Date 14:28 25.03.2022
# Copyright (c) 2022 S. A. Ditlefsen
# License: http://opensource.org/licenses/gpl-license.php GNU Public License
#
###

from random import seed
from random import randint


class Drawer:
    __main_numbers_list = []
    __sub_numbers_list = []
    __gain = 0

    def __init__(self):
        print("\n--- Drawer: ---")
        # self.draw_main_numbers()
        # self.draw_sub_number()
        # self.print_numbers()
        # self.check_if_won(coupong)

    def draw_main_numbers(self):
        # Draw 7 main numbers
        self.__main_numbers_list = []
        for n in range(7):
            number = self.random_unique_integer(self.__main_numbers_list)
            self.__main_numbers_list.append(number)

        # Sort numbers
        self.__main_numbers_list.sort()

    def random_unique_integer(self, existing_numbers):
        value = randint(1, 34)

        if value in existing_numbers:
            return self.random_unique_integer(existing_numbers)
        else:
            return value

    def draw_sub_number(self):
        self.__sub_numbers_list = []
        number = self.random_unique_integer(self.__main_numbers_list)
        self.__sub_numbers_list.append(number)

    # Print main and sub numbers ----
    def print_numbers(self):
        print("Main numbers:")
        for x in self.__main_numbers_list:
            print("[" + str(x) + "]", end=" ")

        print("\nSub numbers:")
        for x in self.__sub_numbers_list:
            print("(" + str(x) + ")", end=" ")

        print("\n")

    def get_main_numbers_list(self):
        return self.__main_numbers_list

    def get_sub_numbers_list(self):
        return self.__sub_numbers_list

    def check_if_won(self, coupong):
        self.__gain = 0
        your_results: list = []
        print("Check if won")

        # 10 rows in coupong to check
        for row in coupong:
            # 7 numbers per row
            main_numbers_correct = 0
            sub_numbers_correct = 0
            gain = 0
            for col in row:

                # Check if my number is
                # part of main or sub

                if col in self.__main_numbers_list:
                    print("[" + str(col) + "]", end=" ")
                    main_numbers_correct += 1
                else:
                    if col in self.__sub_numbers_list:
                        print("(" + str(col) + ")", end=" ")
                        sub_numbers_correct += 1

                    else:
                        print(str(col), end=" ")

            print("\t" + str(main_numbers_correct) + "+" + str(sub_numbers_correct), end="")
            your_results.append(str(main_numbers_correct) + "+" + str(sub_numbers_correct))

            # Check gain
            if main_numbers_correct == 7:
                gain = 14039045
            elif main_numbers_correct == 6 and sub_numbers_correct == 1:
                gain = 165105
            elif main_numbers_correct == 6:
                gain = 4315
            elif main_numbers_correct == 5:
                gain = 110
            elif main_numbers_correct == 4:
                gain = 50
            if gain > 0:
                self.__gain = self.__gain + gain
                print(" " + str(gain), end="")
            print("")

        return your_results

    def get_gain(self):
        return self.__gain