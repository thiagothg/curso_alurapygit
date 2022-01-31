import requests

class BuscaCep:
    def __init__(self, cep):
        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError('Cep inválido!')

    def __str__(self):
        return self.formata_cep()

    def valida_cep(self, cep):
        return True if len(str(cep)) == 8 else False

    def formata_cep(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def buscar_cep(self):
        url = 'https://viacep.com.br/ws/{}/json/'.format(self.cep)
        data = requests.get(url).json()
        print(data['complemento'])

