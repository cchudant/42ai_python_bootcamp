import sys

if len(sys.argv) > 1:
    print(' '.join(map(lambda c: c[::-1].swapcase(), sys.argv[1:][::-1])))
