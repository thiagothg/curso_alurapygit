from cpf_cnpj import Documento
from telefones_br import Telefone
from datas import DataBr
from cep import BuscaCep

print('******** cpf/cnpj ***********')
cpf1 = 44468328835
cpf = Documento.criar_documento(cpf1)

print(cpf)

cnpj1 = "29565153000168"
cnpj = Documento.criar_documento(cnpj1)
print(cnpj)

print('******** telefone ***********')

tel = '2211987140216'
telefone = Telefone(tel)

print(telefone)

print('******** datas ***********')

data = DataBr()
print(data.tempo_cadastro())

print('******** cep ***********')

cep = '09430190'
end = BuscaCep(cep)

print(end.buscar_cep())
