from tokenizador import tokenizar_expressao

def obter_expressao():
    print('Digite a expressão a ser resolvida')
    expressao = input('--> ')
    
    tokens = tokenizar_expressao(expressao)
    print(tokens)