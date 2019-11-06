import time
from random import randint
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


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
