import re

def tokenizar_expressao(expressao):
    """
        Realiza a tokenização da expressão (separar cada elemento da expressão em uma lista)
        
        INPUTS:
            - Expressão 
        
        OUTPUTS:
            - Lista de tokens
    """    
    padrao = r'\d+(?:\.\d+)?|[+\-*/()]'
    
    tokens = re.findall(padrao, expressao)
    
    expressao_limpa = "".join(expressao.split())
    tokens_unidos = "".join(tokens)
        
    return tokens, expressao_limpa, tokens_unidos