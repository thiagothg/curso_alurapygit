class Produto(object):
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    def __repr__(self):
        return "nome:%s valor:%s" % (self.__nome, self.__valor)

    def get_nome(self):
        return self.__nome

    def get_valor(self):
        return self.__valor


lista_produtos = [
  {
    'nome': 'chocolate',  'valor': 3.45
  },
  {
    'nome': 'biscoito', 'valor': 2.49
  },
  {
    'nome': 'cafe', 'valor': 3.45,
  },
  {
    'nome': 'suco', 'valor': 4.3,
  },
  {
    'nome': 'feijao', 'valor': 10.0
  },
  {
    'nome': 'arroz', 'valor': 8.5
  }
]

numeros = [4, 2, 6, 1, 3]
numeros_ordenados = sorted(numeros)

print(numeros)
print(numeros_ordenados)

palavras = ["chocolate", "biscoito", "cafe", "suco", "feijao", "arroz"]
palavras_ordenadas = sorted(palavras)

print(palavras)
print(palavras_ordenadas)
print('**************')

for prod in lista_produtos:
  print(prod['nome'])

produtos_ordenados = sorted(lista_produtos, key = Produto.get_valor)


