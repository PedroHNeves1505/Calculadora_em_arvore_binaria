# Módulo: conversor.py

def precedencia(operador):
    """
        Retorna o nível de prioridade do operador.

        INPUT:
            - Operador
            
        OUTPUT:
            - Valor de prioridade do operador
    """
    if operador in ('*', '/'):
        return 2
    if operador in ('+', '-'):
        return 1
    return 0

def conversor_posfixa(tokens):
    """
    Converte uma lista de tokens da notação infixa para a pós-fixa (RPN)
    usando o algoritmo Shunting Yard.
    
    INPUT:
        - Tokens da operação
        
    OUTPUT:
        - Operação em ordem pós-fixa
    """
    operacao_pos_fixa = []
    pilha = []
    
    for token in tokens:
        if token.replace('.', '', 1).isdigit():
            operacao_pos_fixa.append(token)
            
        elif token == '(':
            pilha.append(token)
            
        elif token == ')':
            while pilha and pilha[-1] != '(':
                operacao_pos_fixa.append(pilha.pop())
            if pilha and pilha[-1] == '(':
                pilha.pop() 
                
        elif token in ('+', '-', '*', '/'):
            while (pilha and pilha[-1] != '(' and 
                precedencia(pilha[-1]) >= precedencia(token)):
                operacao_pos_fixa.append(pilha.pop())
            pilha.append(token)

    while pilha:
        operacao_pos_fixa.append(pilha.pop())
        
    return operacao_pos_fixa