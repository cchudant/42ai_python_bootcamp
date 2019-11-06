import time
from getpass import getuser


def log(func):
    def fn(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        exec_time = time.time() - start

        name = ' '.join(p.capitalize() for p in func.__name__.split('_'))
        with open('machine.log', 'a') as logfile:
            logfile.write('({})Running: {}\t\t[ exec-time = {:.3f} ms ]\n'
                  .format(getuser(), name, exec_time * 1000))

        return res

    fn.__name__ = func.__name__
    return fn
