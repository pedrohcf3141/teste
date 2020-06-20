import os
import simplejson as json
from aluguel import Aluguel
from flask import (
    Flask,
    request,
    jsonify
)

app = Flask(__name__)

@app.route('/calc')
def pega_dados():
    a = Aluguel()
    dados = json.loads(request.args.get("dados"))
    a.dia = int(dados['dia'])
    a.valor = float(dados['valor_nominal'])

    #return str(jsonify(a.custo))
    return str(a) + '"' + str(a.custo).replace("'",'\\"') + '"'
