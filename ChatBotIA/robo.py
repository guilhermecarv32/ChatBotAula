from  chatterbot import ChatBot
import time

CONFIANCA_MINIMA = 0.70

def configurar():
    time.clock = time.time
    robo = ChatBot("Robô de Atendimento do IFBA", read_only= True, logic_adapters = [{"import_path": "chatterbot.logic.BestMatch"}])
    
    return True, robo

def executar(robo):
    while True:
        mensagem = input("Digite alguma coisa...\n")
        resposta = robo.get_response(mensagem.lower())
        if resposta.confidence >= CONFIANCA_MINIMA:
            print(f"IFBA>> {resposta.text}")
        else:
            print("Infelizmente, não sei responder essa pergunta.")
            print("Pergunte outra coisa")
    
if __name__ == "__main__":
    configurado, robo = configurar()
    
    if configurado:
        executar(robo)