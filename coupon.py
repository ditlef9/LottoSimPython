from random import seed
from random import randint


class Coupon:
    __coupon_list = []

    def __init__(self):
        print("\n--- Coupon: ---")

        self.pick_numbers()
        self.print_coupon()

    def pick_numbers(self):
        # Create 10 rows with 7 numbers
        for r in range(10):

            # Pick random numbers
            new_row_numbers = []
            for x in range(7):
                number = self.random_unique_integer(new_row_numbers)
                new_row_numbers.append(number)

            # Append the new row to rows
            new_row_numbers.sort()
            self.__coupon_list.append(new_row_numbers)

    def random_unique_integer(self, row_numbers):
        value = randint(1, 34)

        if value in row_numbers:
            return self.random_unique_integer(row_numbers)
        else:
            return value

    def print_coupon(self):
        for row in self.__coupon_list:
            print(row)

    def __iter__(self):
        """ Iterates over coupon. Will return itself. """
        self.current = 0
        return self

    def __next__(self):
        """ Goes to next coupon. When next is not available it will stop iteration. """
        while self.current != len(self.__coupon_list):
            self.current += 1
            return self.__coupon_list[self.current - 1]
        raise StopIteration