from datetime import datetime,timedelta


class DataBr:
    def __init__(self):
        self.dat_cadastro = datetime.today() - timedelta(days=392, hours=33)

    def __str__(self):
        return self.formata_data()

    def formata_data(self):
        return self.dat_cadastro.strftime('%d/%m/%Y %H:%M')

    def tempo_cadastro(self):
        return datetime.today() - self.dat_cadastro

