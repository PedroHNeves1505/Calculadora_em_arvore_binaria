import re

def obter_expressao():
    print('Digite a expressão a ser resolvida')
    expressao = input('--> ')
    
    tokens = tokenizar_expressao(expressao)
    print(tokens)

def tokenizar_expressao(expressao):
    tokens = re.findall(r'\d+|\S', expressao)
    return tokens  