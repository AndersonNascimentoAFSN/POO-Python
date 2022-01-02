class Retangle:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__area = x * y

    def obter_area(self):
        return self.__area


r = Retangle(7, 6)
# r._Retangle__area = 7
r.raio = 2
print(r.raio)
print(r.obter_area())
