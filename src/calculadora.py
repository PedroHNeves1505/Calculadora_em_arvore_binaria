from .tokenizador import tokenizar_expressao
import time
import os
import subprocess

def obter_expressao_e_tokens():
    """
        Obtem a expressão do usuário, verifica se possui uma expressão digitada e se não possui caracteres indefinidos e realiza a tokenização da expressão
        
        INPUT:
            - Expressão
        
        OUTPUT:
            - Expressão e tokens
    """
    while True:
        print('Digite a expressão a ser resolvida')
        expressao = input('--> ')
        
        if expressao and expressao.strip():
            pass
        else:
            print('A expressão está vazia!')
            time.sleep(3)
            subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
            continue
            
        tokens, expressao_limpa, tokens_unidos = tokenizar_expressao(expressao)
        
        if len(expressao_limpa) != len(tokens_unidos):
                print("A expressão contém caracteres inválidos.")
                time.sleep(3)
                subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
        else:
            return expressao, tokens

def testar_expressao(expressao):
    """
        Realiza os testes de funções pré-definidas
        
        INPUT:
            - Expressão
            
        OUTPUT:
            - Expressão e tokens
    """
    tokens = tokenizar_expressao(expressao)
    return expressao, tokens
    
def pre_ordem(no):
    """
        Retorna uma lista com o percurso em pré-ordem (Raiz, Esquerda, Direita).
    
    INPUT:
        - No
    
    OUTPUT:
        - Lista com expressão pré-ordem
    """
    if no is None:
        return []
    return [no.valor] + pre_ordem(no.esquerda) + pre_ordem(no.direita)

def em_ordem(no):
    """
        Retorna uma lista com o percurso em ordem (In-order).
        
        INPUT: 
            - No
        
        OUTPUT: 
            - Lista com ordem da expressão
    """
    if no is None:
        return []
    return em_ordem(no.esquerda) + [no.valor] + em_ordem(no.direita)

def pos_ordem(no):
    """
        Retorna uma lista com o percurso em pós-ordem (Esquerda, Direita, Raiz).
        
    INPUT:
        - No
    
    OUTPUT:
        - Lista com expressão pós-ordem    
    """
    if no is None:
        return []
    return pos_ordem(no.esquerda) + pos_ordem(no.direita) + [no.valor]

def gerar_expressao(no):
    """
    Reconstrói a expressão infixa a partir da árvore, 
    adicionando parênteses nos nós operadores para manter a precedência.
    
    INPUT:
        - No
    
    OUTPUT:
        - Expressão original recriada
    """
    if no is None:
        return ""
    
    if no.esquerda is None and no.direita is None:
        return str(no.valor)
    
    esq = gerar_expressao(no.esquerda)
    dir = gerar_expressao(no.direita)
    
    return f"({esq} {no.valor} {dir})"

def calcular(no):
    """
    Calcula recursivamente o valor da expressão a partir da árvore binária.
    
    INPUT:
        - No
    
    OUTPUT:
        - Operação calculada
    """
    if no is None:
        return 0
    
    if no.esquerda is None and no.direita is None:
        try:
            if '.' in str(no.valor):
                return float(no.valor)
            return int(no.valor)
        except ValueError:
            return float(no.valor)
            
    valor_esquerda = calcular(no.esquerda)
    valor_direita = calcular(no.direita)
    
    if valor_esquerda == 'reiniciar' or valor_direita == 'reiniciar':
        return 'reiniciar'
    
    operador = no.valor
    if operador == '+':
        return valor_esquerda + valor_direita
    elif operador == '-':
        return valor_esquerda - valor_direita
    elif operador == '*':
        return valor_esquerda * valor_direita
    elif operador == '/':
        if valor_direita == 0:
            return('reiniciar')
        return valor_esquerda / valor_direita