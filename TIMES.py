# Essa classe serve para trabalharmos com o uso de times , podendo adicionar troféus a medida que eles vão vencendo.
class Time:
    def __init__(self, nome, torcida,torneios):
        self._nome = nome.title()
        self.torcida = torcida
        self._torneios = torneios

    @property
    def torneios(self):
        return self._torneios

    def ganha_torneios(self):
        self._torneios += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f'Nome: {self.nome} Torneios: {self.torneios}'

barcelona = Time('Barcelona',10000000,80)
barcelona.ganha_torneios()
print(f'O {barcelona.nome} tem uma torcida de {barcelona.torcida} e tem {barcelona.torneios} troféus')


