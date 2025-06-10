from pymongo import MongoClient
# Conectar ao MongoDB (localhost na porta padrão 27017)
client = MongoClient("mongodb://localhost:27017/")
# Selecionar o banco de dados e a coleção
db = client['meu_banco_de_dados']
colecao = db['minha_colecao']

#--------------------------------------------------

#documento = {
#    "nome": "Roberto Cândido",
#    "idade": 30,
#    "profissao": "Desenvolvedor"
#}

# Inserir um único documento
#resultado = colecao.insert_one(documento)
#print("Documento inserido com o ID:", resultado.inserted_id)

#documentos = [
#    {"nome": "Ana", "idade": 25, "profissao": "Engenheira"},
#    {"nome": "Carlos", "idade": 40, "profissao": "Arquiteto"}
#]
#
#resultado = colecao.insert_many(documentos)
#print("IDs dos documentos inseridos:", resultado.inserted_ids)

#--------------------------------------------------

#busca = colecao.find() #.find para listar todos os documentos

#for doc in busca:
#    print(doc)

#--------------------------------------------------

# Buscar um único documento
#documento = colecao.find_one({"nome": "Roberto Cândido"})
#print("Documento encontrado:", documento)

#--------------------------------------------------

# Buscar múltiplos documentos
#documentos = colecao.find({"idade": {"$gt": 20}})
#for doc in documentos:
#    print(doc)

#--------------------------------------------------

#documentos = colecao.find({"idade": {"$gt": 18}}) #filtro buscar por nome

#for doc in documentos:
#    print(doc['nome'])
#    print(doc['idade'])

#--------------------------------------------------

# Atualizar um único documento
#resultado = colecao.update_one(
#   {"nome": "José Roberto"}, # Filtro
#   {"$set": {"idade": 31}} # Atualização
#)
#print("Número de documentos modificados:", resultado.modified_count)

# Atualizar múltiplos documentos
#resultado = colecao.update_many(
#   {"idade": {"$lt": 30}}, # Filtro
#   {"$set": {"status": "jovem"}} # Atualização
#)
#print("Número de documentos modificados:", resultado.modified_count)

#--------------------------------------------------

# Remover um único documento
#resultado = colecao.delete_one({"nome": "José Roberto"})
#print("Número de documentos deletados:", resultado.deleted_count)

# Remover múltiplos documentos
#resultado = colecao.delete_many({"idade": {"$lt": 30}})
#print("Número de documentos deletados:", resultado.deleted_count)

#--------------------------------------------------

#Inserções em Lote com insert_many
#documentos = [
#    {"nome": "Maria", "idade": 28, "profissao": "Designer"},
#    {"nome": "Pedro", "idade": 35, "profissao": "Analista"},
#    {"nome": "Ana", "idade": 22, "profissao": "Estagiária"}
#]
#resultado = colecao.insert_many(documentos)
#print("IDs dos documentos inseridos:", resultado.inserted_ids)

#--------------------------------------------------

# Buscar todos com idade maior que 25 e profissão 'Designer' ou 'Analista'
#filtro = {
#    "idade": {"$gt": 25},
#    "profissao": {"$in": ["Designer", "Analista"]}
#}
#resultados = colecao.find(filtro)
#
#for doc in resultados:
#    print(doc)

#--------------------------------------------------

# Buscar documentos, mas retornar apenas os campos 'nome' e 'idade'
#projecao = {"_id": 0, "nome": 1, "idade": 1} # 1 para incluir, 0 para excluir

#resultados = colecao.find({}, projection=projecao)
#for doc in resultados:
#    print(doc)

#--------------------------------------------------

# Ordenar por idade (crescente) e depois por nome (decrescente)
resultados = colecao.find().sort([("idade", 1), ("nome", -1)])
for doc in resultados:
    print(doc)


#--------------------------------------------------
