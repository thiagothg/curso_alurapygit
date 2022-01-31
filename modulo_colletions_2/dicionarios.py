"""# Dicionário (Mapa etc)"""
from collections import defaultdict, Counter

aparicoes = {
    "Guilherme": 1,
    "cachorro": 2,
    "nome": 2,
    "vindo": 1
}

type(aparicoes)

aparicoes["Guilherme"]

aparicoes["cachorro"]

# aparicoes["xpto"]

aparicoes.get("xpto", 0)

aparicoes.get("cachorro", 0)

aparicoes = dict(Guilherme=2, cachorro=1)
aparicoes

aparicoes = {"Guilherme": 1, "cachorro": 2, "nome": 2, "vindo": 1}

aparicoes["Carlos"] = 1

aparicoes

aparicoes["Carlos"] = 2

aparicoes

del aparicoes["Carlos"]

aparicoes

"cachorro" in aparicoes

"Carlos" in aparicoes

for elemento in aparicoes:
    print(elemento)

for elemento in aparicoes.keys():
    print(elemento)

for elemento in aparicoes.values():
    print(elemento)

1 in aparicoes.values()

for elemento in aparicoes.keys():
    valor = aparicoes[elemento]
    print(elemento, valor)

for elemento in aparicoes.items():
    print(elemento)

for chave, valor in aparicoes.items():
    print(chave, "=", valor)

["palavra {}".format(chave) for chave in aparicoes.keys()]


meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"

aparicoes = {}

for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)

print('utilizando defaultdict')

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    aparicoes[palavra] += 1

print(aparicoes)

print('utilizando Counter')

aparicoes = Counter(meu_texto.split())
print(aparicoes)


