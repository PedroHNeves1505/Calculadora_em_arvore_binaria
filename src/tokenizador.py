import re

def tokenizar_expressao(expressao):
    tokens = re.findall(r'\d+|\S', expressao)
    return tokens  