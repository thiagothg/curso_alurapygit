from dominio import Usuario, Lance, Leilao, Avaliador

thiago = Usuario('Thiago')
tedd = Usuario('tedd')

lance_thiago = Lance(thiago, 122)
lance_tedd = Lance(tedd, 150)

leilao = Leilao('Celular')

leilao.lances.append(lance_thiago)
leilao.lances.append(lance_tedd)

for lance in leilao.lances:
    print('O usuario {} e lance: {}'.format(lance.usuario.nome, lance.valor))


avaliador = Avaliador()
avaliador.avalia(leilao)

print('O menor lance foi de {} e o maior lance foi de {}'.format(avaliador.menor_lance, avaliador.maior_lance))


