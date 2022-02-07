from test_unitario.leilao.dominio import Usuario, Leilao
import pytest
from test_unitario.leilao.excecoes import LanceInvalido

class TestUsuario:
    @pytest.fixture()
    def thiago(self):
        return Usuario('Thiago', 100)

    @pytest.fixture()
    def leilao(self):
        return Leilao('Celular')

    def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(self, thiago, leilao):
        thiago.propoe_lance(leilao, 50)

        assert thiago.carteira == 50

    def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(self, thiago, leilao):
        thiago.propoe_lance(leilao, 1.0)

        assert thiago.carteira == 99.0


    def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(self, thiago, leilao):
        thiago.propoe_lance(leilao, 100.0)

        assert thiago.carteira == 0.0


    def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira(self, thiago, leilao):
        with pytest.raises(LanceInvalido):

            thiago.propoe_lance(leilao, 200.0)