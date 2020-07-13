from unittest import TestCase
from aluguel import Aluguel


class AluguelTeste(TestCase):
    def teste_dez(self):
        aluguel = Aluguel()
        aluguel.dia = 1
        self.assertEqual({"valor_calculado": 450.0}, aluguel.custo)
        aluguel.dia = 2
        aluguel.valor= 500
        self.assertEqual({"valor_calculado": 450.0}, aluguel.custo)
        aluguel.dia = 5
        aluguel.valor = 500
        self.assertEqual({"valor_calculado": 450.0}, aluguel.custo)
    def teste_cinco(self):
        aluguel = Aluguel()
        aluguel.dia = 6
        self.assertEqual({"valor_calculado": 475.0}, aluguel.custo)
        aluguel.dia = 7
        aluguel.valor = 500
        self.assertEqual({"valor_calculado": 475.0}, aluguel.custo)
        aluguel.dia = 10
        aluguel.valor = 500
        self.assertEqual({"valor_calculado": 475.0}, aluguel.custo)
    def teste_normal(self):
        aluguel = Aluguel()
        aluguel.dia = 11
        self.assertEqual({"valor_calculado": 500.0}, aluguel.custo)
        aluguel.dia = 12
        aluguel.valor = 500
        self.assertEqual({"valor_calculado": 500.0}, aluguel.custo)
        aluguel.dia = 15
        aluguel.valor = 500
        self.assertEqual({"valor_calculado": 500.0}, aluguel.custo)
    def teste_multa(self):
        aluguel = Aluguel()
        aluguel.dia = 16
        self.assertEqual({"valor_calculado": 510.5}, aluguel.custo)
        aluguel.dia = 22
        aluguel.valor = 500
        self.assertEqual({"valor_calculado": 513.5}, aluguel.custo)
        aluguel.dia = 30
        aluguel.valor = 500
        self.assertEqual({"valor_calculado": 517.5}, aluguel.custo)
    def teste_invalido_mais(self):
        aluguel = Aluguel()
        aluguel.dia = 31
        self.assertEqual({"valor_calculado": -1}, aluguel.custo)
    def teste_invalido_menos(self):
        aluguel = Aluguel()
        aluguel.dia = 0
        self.assertEqual({"valor_calculado": -1}, aluguel.custo)
