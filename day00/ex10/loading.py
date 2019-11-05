import os
from time import time

def ft_progress(ite):
    def get_term_width():
        rows, columns = os.popen('stty size', 'r').read().split()
        return int(columns)

    l = len(ite)
    start = time()
    i = 0
    for el in ite:
        elapsed = time() - start
        eta = elapsed / (i + 1) * l - elapsed
        percent = (i + 1) / l
        term_width = get_term_width()

        right_txt = 'ETA: {:.2f}s [{:>3.0f}%]['.format(eta, percent * 100)
        left_txt = '] {0:>{1}}/{2} | elapsed time {3:.2f}s'.format(
                i + 1, len(str(l)), l, elapsed)
        mid_len = term_width - len(right_txt) - len(left_txt)

        mid_txt = '=' * int((mid_len - 1) / l * (i + 1)) + '>'

        print('{0}{1:{2}}{3}'.format(right_txt, mid_txt, mid_len, left_txt),
                end='\r')

        yield el
        i += 1


from time import sleep
listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)
