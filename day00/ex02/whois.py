import sys

if len(sys.argv) == 2 and sys.argv[1].isdigit():
    i = int(sys.argv[1])
    if i == 0:
        print('I\'m Zero.')
    elif i % 2 == 0:
        print('I\'m Even.')
    else:
        print('I\'m Odd.')
elif len(sys.argv) != 1:
    print('ERROR')
