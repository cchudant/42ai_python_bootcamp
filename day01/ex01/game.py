
class GotCharacter():
    """A Game Of Thrones character"""

    def __init__(self, first_name=None, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    """The Stark family"""

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False
