from pymongo import MongoClient
from flask import Flask, jsonify, request

client = MongoClient('localhost')
db = client['basededados']
col = db['pessoas']
app = Flask("Teste")
    


#GET ALL
@app.route("/listar", methods=["GET"])
def listarElementos():
    data = []
    for q in col.find():
        data.append({
                    'nome': q['nome'],
                    'email': q['email'],
                    'telefone': q['telefone'],
                    'endereco': q['endereco'] 
                    }) 
    return jsonify(data)


#GET NOME
@app.route("/listar/<nome>", methods=["GET"])
def listarElementoPorNome(nome):   
    q = col.find_one({'nome': nome})
    if q:
        data = {
                'nome': q['nome'],
                'email': q['email'],
                'telefone': q['telefone'],
                'endereco': q['endereco'] 
                }
    else:
        data = 'Sem resultados'
    return jsonify(data) 


#POST PESSOA
@app.route("/listar", methods=["POST"])
def cadastrarElementos():    
    nome = request.json['nome']
    email = request.json['email']
    telefone = request.json['telefone']
    endereco = request.json['endereco']
    data = {
            'nome': nome,
            'email': email,
            'telefone': telefone,
            'endereco': endereco 
            }
    pessoa = col.insert(data)
    return "Dados Enviados"       


#PUT PESSOA
@app.route("/listar/<nome>", methods=["PUT"])
def atualizarElementoPornome(nome):   
    q = col.find_one({'nome': nome})
    if q:
        nomebody = request.json['nome']
        email = request.json['email']
        telefone = request.json['telefone']
        endereco = request.json['endereco']      
        col.update_one(
            {
            "nome": nome
            },
            {
                "$set": {
                    "nome":nomebody,
                    "email":email,
                    "telefone":telefone,
                    "endereco":endereco
                }
            }    
            )
        resposta = "Atualizado com sucesso"       
    else:
        resposta = "Erro ao atualizar"
    return resposta   


#DELETE PESSOA
@app.route("/listar/<nome>", methods=["DELETE"])
def deletarElementoPornome(nome):   
    q = col.find_one({'nome': nome})
    if q:
        col.delete_one({
            "nome":nome
        })
        resposta = 'Deletado com sucesso'
    else:
        resposta = 'Não foi possivel deletar'
    return jsonify(resposta)


app.run()





