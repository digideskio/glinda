import random
from getch import getch
import math


class Mergesorter(object):
    def __init__(self, items):
        self.items = items[:]
        random.shuffle(self.items)
        lg_n = math.ceil(math.log(len(self.items), 2))
        self.remaining = self.original = len(self.items) * lg_n - 2 * lg_n + 1

    def compare(self, left, right):
        print
        print '1. %s' % str(left)
        print '2. %s' % str(right)
        choice = ''
        while True:
            choice = getch()
            if choice == 'q':
                raise KeyboardInterrupt()
            if choice and choice[0] in '12':
                break

        self.remaining -= 1
        print('at most %d remaining of %d (%f%%)' %
              (self.remaining, self.original,
               float(self.remaining)/self.original * 100))
        return {'1': -1, '2': 1}[choice[0]]

    def merge(self, left, right):
        result = []
        while left and right:
            if self.compare(left[0], right[0]) <= 0:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]

        result += left
        result += right
        return result

    def sort(self, items=None):
        if items is None:
            items = self.items

        if len(items) <= 1:
            return items
        else:
            return self.merge(self.sort(items[:len(items)/2]),
                              self.sort(items[len(items)/2:]))


def mergesort(items):
	return Mergesorter(items).sort()

