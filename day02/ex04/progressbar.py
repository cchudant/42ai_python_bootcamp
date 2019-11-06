import os
from time import time


def progressbar(ite):
    def get_term_width():
        rows, columns = os.popen('stty size', 'r').read().split()
        return int(columns)

    ll = len(ite)
    start = time()
    i = 0
    for el in ite:
        elapsed = time() - start
        eta = elapsed / (i + 1) * ll - elapsed
        percent = (i + 1) / ll
        term_width = get_term_width()

        right_txt = 'ETA: {:.2f}s [{:>3.0f}%]['.format(eta, percent * 100)
        left_txt = '] {0:>{1}}/{2} | elapsed time {3:.2f}s'.format(
                i + 1, len(str(ll)), ll, elapsed)
        mid_len = term_width - len(right_txt) - len(left_txt)

        mid_txt = '=' * int((mid_len - 1) / ll * (i + 1)) + '>'

        print('{0}{1:{2}}{3}'.format(right_txt, mid_txt, mid_len, left_txt),
              end='\r')

        yield el
        i += 1
