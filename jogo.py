class Jogo:
    def __init__(self, nome, vezes_que_joguei):
        self.__nome = nome
        self.__vezes_que_joguei = vezes_que_joguei

    def get_vezes_jogo(self):
        print(self.__vezes_que_joguei)

    def set_vezes_jogo(self, valor):
        self.__vezes_que_joguei = valor


jogador = Jogo('Guilherme', 2)
jogador.get_vezes_jogo()
jogador.set_vezes_jogo(3)
jogador.get_vezes_jogo()
