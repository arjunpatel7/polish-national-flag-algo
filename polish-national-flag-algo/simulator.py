import numpy as np
import pandas as pd
import random


class PolishCheckers:
    # an instance of the polish national flag problem game.
    # We'll represent red as 0 and black as 1


    def __init__(self, num_checkers):
        self.checkers = random.choices([0, 1],  k=num_checkers)
        self.num_swaps = 0
        self.num_inspections = 0
        self.history = []
        self.win = False

    def inspect(self, c1, c2):
        checker_1 = self.checkers[c1]
        checker_2 = self.checkers[c2]
        self.num_inspections += 2
        return checker_1 < checker_2
    def swap(self, c1, c2):
        # swap the locations of two checkers
        # accepts index of each checker
        checker_1 = self.checkers[c1]
        checker_2 = self.checkers[c2]
        self.checkers[c2] = checker_1
        self.checkers[c1] = checker_2
        self.num_swaps += 2

    def win_condition(self):
        sorted_checkers = list(sorted(self.checkers))
        self.win = sorted_checkers == self.checkers


    def print_status(self):
        print(self.checkers)
    # merge sort

    # quick sort

    # bubble sort

    def bubble_sort(self):
        self.win_condition()
        while not self.win:
            # move along the entries until each pair is either swapped or not
            for c_ind in range(0, len(self.checkers)-1):
                pc.print_status()
                if not self.inspect(c_ind, c_ind + 1):
                    self.swap(c_ind, c_ind + 1)
            self.win_condition()
        pc.print_status()
        print("Number of swaps: ", self.num_swaps)
        print("Number of inspections: ", self.num_inspections)
        return [self.num_swaps, self.num_inspections]




for x in range(0, 5):
    pc = PolishCheckers(15)
    pc.print_status()
    print(pc.bubble_sort())
