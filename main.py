import sort

"""
options = [
	'Crothers',
	'FloMo',
	'Lag',
	'Manz',
	'GovCo',
	'Academic theme',
	'Co-op',
	'Self-op',
	'Cultural theme',
	'Apartment'
]
"""

def displayComparison(comparison):
	print ('1. %s' % comparison[0])
	print ('2. %s' % comparison[1])

def getChoice():
	while True:
		c = raw_input()
		if c and c[0] in '12':
			break
		print ('Please enter 1 or 2.')
	
	return int(c[0])

def displayState(state):
	pass

def displayResults(results):
	for entry in results:
		print (entry)

'''
sorting = sort.start(options)
while True:
	comparison = sorting.next()
	if comparison is None:
		break
	displayComparison(comparison)
	sorting.choose(getChoice())
	displayState(sorting.state())

displayResults(sorting.results())
'''

def loadFrom(filename):
    with open(filename, 'r') as optionsFile:
        return [option[:-1] for option in optionsFile if option not in ('', '\n')]

def writeResultTo(options, filename):
    with open(filename, 'w') as outputFile:
        outputFile.writelines([option + '\n' for option in options])

if __name__ == '__main__':
    options = loadFrom('options.txt')
    try:
        options = sort.mergesort(options)
    finally:
        writeResultTo(options, 'result.txt')

