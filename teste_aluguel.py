from unittest import TestCase
from aluguel import Aluguel


class AluguelTeste(TestCase):
    def teste_dez(self):
        aluguel = Aluguel()
        aluguel.dia = 2        
        self.assertEqual({"valor_calculado": 450.0}, aluguel.custo)
    def teste_cinco(self):
        aluguel = Aluguel()
        aluguel.dia = 6
        self.assertEqual({"valor_calculado": 475.0}, aluguel.custo)
    def teste_normal(self):
        aluguel = Aluguel()
        aluguel.dia = 11
        self.assertEqual({"valor_calculado": 500.0}, aluguel.custo)
    def teste_multa(self):
        aluguel = Aluguel()
        aluguel.dia = 16
        self.assertEqual({"valor_calculado": 510.5}, aluguel.custo)
    def teste_invalido_mais(self):
        aluguel = Aluguel()
        aluguel.dia = 32
        self.assertEqual({"valor_calculado": -1}, aluguel.custo)
    def teste_invalido_zero(self):
        aluguel = Aluguel()
        aluguel.dia = 0
        self.assertEqual({"valor_calculado": -1}, aluguel.custo)
