
class Client:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name.title()

    @
    def name(self, name):
        self.__name = name
