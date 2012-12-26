import sort


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

