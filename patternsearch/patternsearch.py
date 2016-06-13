import re
import sys

def main():
    """Calculate the number of times a pattern appears in a string."""
    first_line = sys.stdin.readline().strip()
    str_len = int(first_line.split()[0])
    pattern_len = int(first_line.split()[1])
    string_input = sys.stdin.readline().strip()
    pattern = sys.stdin.readline().strip()
    pattern = pattern.replace('*', '.{1}')
    pattern = '(?=({pattern}))'.format(pattern=pattern)
    matches = re.findall(pattern, string_input)
    print len(matches)


if __name__ == '__main__':
    main()