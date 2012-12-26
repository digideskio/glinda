import sort


def load_from(filename):
    with open(filename, 'r') as options_file:
        return [option[:-1] for option in options_file if option not in ('', '\n')]


def write_result_to(options, filename):
    with open(filename, 'w') as output_file:
        output_file.writelines([option + '\n' for option in options])


if __name__ == '__main__':
    options = load_from('options.txt')
    try:
        options = sort.mergesort(options)
    finally:
        write_result_to(options, 'result.txt')
