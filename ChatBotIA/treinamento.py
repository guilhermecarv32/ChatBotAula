from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json
import time

CONVERSAS = [
    "conversas/saudacoes.json"
]

#1. devolve um treinador de robo
def configurar():
    time.clock = time.time
    
    robo = ChatBot("Robô de Atendimento do IFBA")
    treinador = ListTrainer(robo)
    
    return True, treinador
    
#2. carrega as conversas a partir do json    
def carregar_conversas():
    carregadas, conversas = True, []
    
    for arquivo_de_conversas in CONVERSAS:
        try:
            with open(arquivo_de_conversas, "r") as arquivo:
                para_treinar = json.load(arquivo)
                conversas.append(para_treinar["conversas"])
                
                arquivo.close()
        except Exception as e:
            carregadas = False
    
    return carregadas, conversas
    
#3. usa o treinador para treinar o robo com as conversas
def treinar(treinador, conversas):
    for conversa in conversas:
        for mensagens_resposta in conversa:
            mensagens = mensagens_resposta["mensagens"]
            resposta = mensagens_resposta["resposta"]
            
            print(f"Treinando o robo, mensagens: {mensagens}, resposta: {resposta}")
            for mensagem in mensagens:
                treinador.train([mensagem, resposta])
    
if __name__ == "__main__":
    configurado, treinador = configurar()
    
    if configurado:
        carregadas, conversas = carregar_conversas()
        if carregadas:
            treinar(treinador, conversas)