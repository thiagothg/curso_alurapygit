from unittest import TestCase

from test_unitario.leilao.dominio import Usuario, Lance, Leilao
from test_unitario.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):
    def setUp(self):
        self.thiago = Usuario('Thiago', 200)
        self.tedd = Usuario('tedd', 250)

        self.lance_thiago = Lance(self.thiago, 122)
        self.lance_tedd = Lance(self.tedd, 150)

        self.leilao = Leilao('Celular')

    def test_avalia_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        self.leilao.propoe(self.lance_thiago)
        self.leilao.propoe(self.lance_tedd)

        menor_valor_esperado = 122
        maior_valor_esperado = 150

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):
        with self.assertRaises(LanceInvalido):
            # self.leilao.propoe(self.lance_tedd)
            # self.leilao.propoe(self.lance_thiago)

            yuri = Usuario('Yuri', 190)
            lance_do_yuri = Lance(yuri, 150.0)

            self.leilao.propoe(self.lance_tedd)
            self.leilao.propoe(lance_do_yuri)


    def test_avalia_quando_tiver_um_lance(self):
        self.leilao.propoe(self.lance_thiago)

        valor_esperado = 122

        self.assertEqual(valor_esperado, self.leilao.menor_lance)
        self.assertEqual(valor_esperado, self.leilao.maior_lance)

    def test_avalia_quando_tiver_tres_lance(self):
        self.andy = Usuario('tedd', 100)
        self.lance_andy = Lance(self.andy, 200)

        self.leilao.propoe(self.lance_thiago)
        self.leilao.propoe(self.lance_tedd)
        self.leilao.propoe(self.lance_andy)

        menor_valor_esperado = 122
        maior_valor_esperado = 200

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_thiago)

        quatidade_de_lances_recebido = len(self.leilao.lances)

        self.assertEqual(1, quatidade_de_lances_recebido)

    def test_deve_permitir_propor_lance_caso_o_ultimo_usuario_seja_diferente(self):
        andy = Usuario('tedd', 200)
        lance_andy = Lance(andy, 200)

        self.leilao.propoe(self.lance_thiago)
        self.leilao.propoe(lance_andy)

        quantidade_de_lances_recebido = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebido)

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_tedd_segundo = Lance(self.tedd, 200)

        # try:
        #
        #     self.leilao.propoe(self.lance_tedd)
        #     self.leilao.propoe(lance_tedd_segundo)
        # except ValueError:
        #     quantidade_de_lances_recebido = len(self.leilao.lances)
        #     self.assertEqual(1, quantidade_de_lances_recebido)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_tedd)
            self.leilao.propoe(lance_tedd_segundo)
