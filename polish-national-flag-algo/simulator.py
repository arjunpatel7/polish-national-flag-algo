import numpy as np
import pandas as pd
import random


class PolishCheckers:
    # an instance of the polish national flag problem game.
    # We'll represent red as 1 and black as 0


    def __init__(self, num_checkers):
        self.checkers = random.choices([0, 1],  k=num_checkers)
        self.num_swaps = 0
        self.num_inspections = 0
        self.history = []
        self.win = False

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






pc = PolishCheckers(5)
pc.print_status()
pc.swap(0, 4)
pc.print_status()
