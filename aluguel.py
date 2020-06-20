"""
Criado por Pedro Henrique Cerqueira Fernandes
Data 19/06/2020
"""

class Aluguel():

    def __init__(self):
        self.valor = 500
        self.dia = 16

    @property
    def custo(self):
        
        cinco = 'cinco'
        dez = 'dez'
        normal = 'normal'
        multa = 'multa'

        aluguel = {
        cinco:[range(1, 6), self.valor * 0.9],
        dez: [range(6, 11), self.valor * 0.95],
        normal: [range(11, 16), self.valor],
        multa: [range(16, 31),
                (self.valor * 1.02) + # multa
                (self.valor *(0.001 * # acrescimo
                              (self.dia-15)))] # diária
        }
        for key in aluguel:
            if self.dia in aluguel[key][0]:
                self.valor = aluguel[key][1]
                break
            else:
                self.valor = -1
        return {"valor_calculado": round(self.valor, 2)}

    def __str__(self):
        return '<h3>Pedro Henrique Cerqueira Fernandes</h3> <br> Informa que está consumindo uma API WEB <br>'
