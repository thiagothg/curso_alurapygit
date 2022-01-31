import re


class Telefone:
    def __init__(self, tel):
        if self.valida_telefone(tel):
            self.numero = tel
        else:
            raise ValueError('Telefone invalido')

    def __str__(self):
        return self.formata_numero()

    def valida_telefone(self, tel):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        res = re.findall(padrao, tel)
        return True if res else False

    def formata_numero(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        res = re.search(padrao, self.numero)
        codigo = '55' if res.group(1) == None else res.group(1)

        numero_formatada = "+{} ({}) {}-{}".format(
            codigo,
            res.group(2),
            res.group(3),
            res.group(4)
        )

        return numero_formatada