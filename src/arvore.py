from no import No

def construir_arvore(posfixa):
    """
    Constrói a árvore binária de expressão a partir de uma lista pós-fixa.
    Retorna a raiz da árvore.
    
    INPUT:
        - Operação pós-fixa
        
    OUTPUT:
        - Construção da árvore binária
    """
    pilha_nos = []
    
    for token in posfixa:
        if token.replace('.', '', 1).isdigit():
            no = No(token)
            pilha_nos.append(no)
            
        elif token in ('+', '-', '*', '/'):
            no_operador = No(token)
            
            no_operador.direita = pilha_nos.pop()
            no_operador.esquerda = pilha_nos.pop()

            pilha_nos.append(no_operador)
            
    return pilha_nos[0] if pilha_nos else None  