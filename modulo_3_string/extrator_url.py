import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanetiza_url(url)

    def sanetiza_url(self, url):
        return url.strip()

    def valida_url(self):
        if not self.url:  # Essa validação já existia
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?: //)?(www.)?bytebank.com(.br)? / cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida.")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return 'URL []'


url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url)

print("O tamanho da URL é: ", len(extrator_url))
print("URL completa: ", extrator_url)

# Verifica que duas instâncias com a mesma URL são iguais
print("extrator_url == extrator_url_2? ", extrator_url == extrator_url_2)

# Busca o valor do parâmetro quantidade
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print("Valor do parâmetro 'quantidade': ", valor_quantidade)

#desafio
valor_dolar = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")


if moeda_origem.lower() == "dolar" and moeda_destino.lower() == "real":
    valor_convertido = valor_dolar * float(quantidade)
elif moeda_origem.lower() == "real" and moeda_destino.lower() == "dolar":
    valor_convertido = float(quantidade) / valor_dolar
else:
    print(f"Câmbio de {moeda_origem} para {moeda_destino} não está disponível.")

print(f"Valor convertido de {moeda_origem} para {moeda_destino} com qtde {quantidade} é {valor_convertido:.2f} {moeda_destino}")