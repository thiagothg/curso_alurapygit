from validate_docbr import CPF, CNPJ

class Documento:
    @staticmethod
    def criar_documento(doc):
        doc = str(doc)
        if len(doc) == 11:
            return DocCpf(doc)
        elif len(doc) == 14:
            return DocCnpj(doc)
        else:
            raise ValueError('Quantidade de digítos esta incorreta')


class DocCpf(Documento):
    def __init__(self, doc):
        if self.valida(str(doc)):
            self.cpf = str(doc)
        else:
            raise ValueError('CPF invalido')

    def __str__(self):
        return self.formata_cpf()

    def valida(self, doc):
        valida = CPF()
        return valida.validate(doc)

    def formata_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class DocCnpj(Documento):
    def __init__(self, doc):
        if self.valida(str(doc)):
            self.cnpj = str(doc)
        else:
            raise ValueError('CNPJ invalido')

    def __str__(self):
        return self.formata_cnpj()

    def valida(self, doc):
        valida = CNPJ()
        return valida.validate(doc)

    def formata_cnpj(self):
        mask = CNPJ()
        return mask.mask(self.cnpj)
