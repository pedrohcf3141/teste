from unittest import TestCase
from aluguel import Aluguel
import csv
from selenium.webdriver import Chrome
from time import sleep

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


class TesteCsv(TestCase):

    def modelo(self, lista):
        aluguel = Aluguel()
        l = list(csv.reader(lista))
        aluguel.dia = int(l[1][0])
        resultado = float(l[0][1])
        self.assertEqual({"valor_calculado": resultado}, aluguel.custo)
        aluguel.dia = int(l[1][1])
        aluguel.valor = int(l[0][0])
        self.assertEqual({"valor_calculado": resultado}, aluguel.custo)
        aluguel.dia = int(l[1][2])
        aluguel.valor = int(l[0][0])
        self.assertEqual({"valor_calculado": resultado}, aluguel.custo)

    def teste_dez_csv(self):
        self.modelo(["500,450.0", "1,2,5"])
    def teste_cinco(self):
        aluguel = Aluguel()
        self.modelo(["500,475.0", "6,7,10"])
    def teste_normal(self):
        self.modelo(["500,500", "11,12,15"])
    def teste_multa(self):
        aluguel = Aluguel()
        aluguel = Aluguel()
        lista = ["500,510.5,513.5,517.5", "16,22,30"]
        l = list(csv.reader(lista))
        aluguel.dia = int(l[1][0])
        resultado = float(l[0][1])
        self.assertEqual({"valor_calculado": resultado}, aluguel.custo)
        aluguel.valor = int(l[0][0])
        aluguel.dia = int(l[1][1])
        resultado = float(l[0][2])
        self.assertEqual({"valor_calculado": resultado}, aluguel.custo)
        aluguel.valor = int(l[0][0])
        aluguel.dia = int(l[1][2])
        resultado = float(l[0][3])
        self.assertEqual({"valor_calculado": resultado}, aluguel.custo)
    def teste_invalido(self):
        self.modelo(["500,-1","31,0,-1"])

class TesteSeleniun(TestCase):

    def modelo(self, d):

        browser = Chrome()
        url = 'https://aluguebug.herokuapp.com/form'
        browser.get(url)
        dia = browser.find_element_by_id("dia")
        v_nominal = browser.find_element_by_id('valor_nominal')

        botao = browser.find_element_by_id('botao')

        dia.send_keys(d)
        v_nominal.send_keys(500)
        botao.click()
        sleep(2)
        v_calculado = browser.find_element_by_id('resposta')
        resposta = v_calculado.get_attribute("value")
        browser.quit()

        aluguel = Aluguel()
        aluguel.dia = d
        resultado = float(resposta)
        self.assertEqual({"valor_calculado": resultado}, aluguel.custo)

    def teste_dez_selenium(self):
        self.modelo(1)
        self.modelo(2)
        self.modelo(5)
    def test_cinco_selenium(self):
        self.modelo(6)
        self.modelo(7)
        self.modelo(10)
    def test_normal_selenium(self):
        self.modelo(11)
        self.modelo(12)
        self.modelo(15)
    def test_multa_selenium(self):
        self.modelo(16)
        self.modelo(22)
        self.modelo(30)
    def test_invalido_selenium(self):
        self.modelo(31)
        self.modelo(-1)
        self.modelo(0)
