import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.tokenizador import tokenizar_expressao
from src.conversor import conversor_posfixa
from src.arvore import construir_arvore
from src.calculadora import calcular, pre_ordem, em_ordem, pos_ordem

def testar_calculo_expressoes(expressao_str):
    """
        Testa o fluxo completo de várias expressões matemáticas.
        
        INPUT:    
            - Expressão e resultado esperado
        
        OUTPUT:
            - Resultado da expressão
    """
    tokens, _, _ = tokenizar_expressao(expressao_str)
    operacao_pos_fixa = conversor_posfixa(tokens)
    arvore = construir_arvore(operacao_pos_fixa)
    
    resultado = calcular(arvore)
    return f'{expressao_str} = {resultado}'
    
if __name__ == '__main__':
    expressoes = [
        '8 + 4 * 2', 
        '(8 + 4) * 2', 
        '((15 - 3) / 4) + (2 * 5)', 
        '((20 / 5) + 3) * (9 - (2 + 1))', 
        '12.5 + 2.5 * 4',
    ]
    
    print("--- A Executar Testes Automatizados ---")
    for expressao in expressoes:
        resultado_teste = testar_calculo_expressoes(expressao)
        print(resultado_teste)