import random
from collections import deque
from getch import getch
import math


remaining = 0
original = 0


def compare(left, right):
	global remaining, original

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

	remaining -= 1
	print 'at most %d remaining of %d (%f%%)' % (remaining, original, float(remaining)/original * 100)
	return {'1': -1, '2': 1}[choice[0]]


def merge(left, right):
	result = []
	while left and right:
		if compare(left[0], right[0]) <= 0:
			result.append(left[0])
			left = left[1:]
		else:
			result.append(right[0])
			right = right[1:]
	
	result += left
	result += right
	return result


def mergesort_rec(items):
	if len(items) <= 1:
		return items
	else:
		return merge(mergesort_rec(items[:len(items)/2]),
					 mergesort_rec(items[len(items)/2:]))


def mergesort(items):
	global remaining, original
	
	random.shuffle(items)
	lg_n = math.ceil(math.log(len(items), 2))
	remaining = original = len(items) * lg_n - 2 * lg_n + 1
	return mergesort_rec(items)

