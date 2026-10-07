from calculadora import obter_expressao_e_tokens
from conversor import conversor_posfixa
from arvore import construir_arvore

def main():
    expressao, tokens = obter_expressao_e_tokens()
    operacao_pos_fixa = conversor_posfixa(tokens)
    arvore = construir_arvore(operacao_pos_fixa)
    print(f'Expressão: {expressao} | Tokens: {tokens} | Operação Pós-fixa: {operacao_pos_fixa} | Árvore: {arvore}')


if __name__ == "__main__":
    main()