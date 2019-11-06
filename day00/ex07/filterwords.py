import re
import string
from sys import argv

if len(argv) != 3 or not argv[2].isdigit() or argv[1].isdigit():
    print('ERROR')
else:
    n = int(argv[2])
    pattern = r'[{} ]'.format(string.punctuation)
    print([el for el in re.split(pattern, argv[1]) if len(el) > n])
