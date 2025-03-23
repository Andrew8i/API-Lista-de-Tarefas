from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Lista com as tarefas
lista_tarefas = [{'id':0, 'responsavel':'Matheus','tarefa':'levar o cachorro pra passear','status':'concluido'}, {'id':1,'responsavel':'João','tarefa':'lavar a louça','status':'pendente'}]

#Metodo que lista todos as tarefas
@app.route('/',methods=['GET'])
def consultar():
    return jsonify(lista_tarefas)

#Metodo para apagar somente o status do id digitado
@app.route('/status/<int:id>',methods=['DELETE'])
def apagar(id):
    dados =  lista_tarefas[id]
    for i in lista_tarefas:
        if i == dados:
            del (i['status'])
    return jsonify('Status excluido com sucesso')

#Metodo para listar apenas pelo id, para editar apenas o status da tarefa e deletar a tarefa por completo pelo id
@app.route('/<int:id>/', methods=['GET', 'PUT','DELETE'])
def metodos(id):
    if request.method == 'GET':
        response = lista_tarefas[id]
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        lista_tarefas[id]['status'] = dados['status']
        return jsonify('Status editado com sucesso', dados)
    elif request.method == 'DELETE':
        lista_tarefas.pop(id)
        return ['Tarefa excluída com sucesso']
    
if __name__ == ('__main__'):
    app.run(debug=True)

