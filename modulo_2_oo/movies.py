class Heranca:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

class Filme(Heranca):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return 'Fime: {} - Ano: {} - Duracao: {} - Likes: {}'.format(self.nome, self.ano, self.duracao, self.likes)


class Serie(Heranca):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return 'Fime: {} - Ano: {} - temporadas: {} - Likes: {}'.format(self.nome, self.ano, self.temporadas, self.likes)


class Playlist():
    def __init__(self, nome, filmes_series):
        self.nome = nome
        # super().__init__(filmes_series)
        self.filmes_series = filmes_series

    def __getitem__(self, item):
        return self.filmes_series[item]

    @property
    def listagem(self):
        return self.filmes_series

    def __len__(self):
        return len(self.filmes_series)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
tmep = Filme('todo mundo em panico', 1999, 100)
tmep.dar_likes()
tmep.dar_likes()
demolidor = Serie('demolidor', 2016, 2)
demolidor.dar_likes()
demolidor.dar_likes()
serie = Serie('atlanta', 2018, 2)
serie.dar_likes()
serie.dar_likes()

playlist = Playlist('Teste', [vingadores, serie])

for item in playlist:
    print(item)


print(len(playlist))

print(repr(playlist))
