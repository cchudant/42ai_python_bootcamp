import sys

def operations(a, b):
    return (
            a + b,
            a - b,
            a * b,
            a / b if b != 0 else 'ERROR (div by zero)',
            a % b if b != 0 else 'ERROR (modulo by zero)'
            )

def usage():
    print('Usage: python', sys.argv[0])
    print('Example:')
    print('    python', sys.argv[0], '10 3')

if len(sys.argv) > 3:
    print('InputError: too many arguments')
    usage()
elif len(sys.argv) < 3:
    usage()
else:
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])

        sum, diff, prod, div, mod = operations(a, b)

        print('Sum:       ', sum)
        print('Difference:', diff)
        print('Product:   ', prod)
        print('Quotient:  ', div)
        print('Modulo:    ', mod)

    except ValueError:
        print('InputError: only numbers')
        usage()
