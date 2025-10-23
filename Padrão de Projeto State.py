class Estado:
    def acao(self):
        pass

class EstadoLigado(Estado):
    def acao(self):
        print("O dispositivo está ligado.")

class EstadoDesligado(Estado):
    def acao(self):
        print("O dispositivo está desligado.")

class Dispositivo:
    def __init__(self):
        self.estado = EstadoDesligado()

    def set_estado(self, estado):
        self.estado = estado

    def acao(self):
        self.estado.acao()

dispositivo = Dispositivo()
dispositivo.acao()

dispositivo.set_estado(EstadoLigado())
dispositivo.acao()
