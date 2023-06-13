class Cola():

    def __init__(self):
        self.__elementos = []

    def arrive(self, value):
        self.__elementos.append(value)

    def atenttion(self):
        if self.size() > 0:
            return self.__elementos.pop(0)

    def size(self):
        return len(self.__elementos)

    def on_front(self):
        if self.size() > 0:
            return self.__elementos[0]

    def move_to_end(self):
        if self.size() > 0:
            aux = self.atention()
            self.arrive(aux)
            return aux