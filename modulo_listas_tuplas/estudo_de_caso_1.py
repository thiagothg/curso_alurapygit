# Onde eu trabalho, todos os links acessados por qualquer computador da empresa
# são armazenados em um mesmo arquivo de registro na rede, o acessos.log,
# para maior controle do que os funcionários andam acessando durante o horário de trabalho.

# registro = open('acesso.log', 'r')
#
# sites_sem_https = [url for url in registro if url.startswith('http://')]
#
# print(sites_sem_https)

class IteradorHttp:
    def __init__(self):
        self.registro = open('acesso.log', 'r')
        self.linha_atual = ''

    def __iter__(self):
        return self

    def __next__(self):
        self.linha_atual = self.registro.readline()
        while self.linha_atual and not self.linha_atual.startswith('http://'):
            self.linha_atual = self.registro.readline()
        if self.linha_atual:
            return self.linha_atual
        raise StopIteration


iterador = IteradorHttp()

for url in iterador:
    print(url)
