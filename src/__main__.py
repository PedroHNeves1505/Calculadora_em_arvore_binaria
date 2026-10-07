from calculadora import obter_expressao_e_tokens
from conversor import conversor_posfixa

def main():
    expressao, tokens = obter_expressao_e_tokens()
    operacao_pos_fixa = conversor_posfixa(tokens)
    print(f'Expressão: {expressao} | Tokens: {tokens} | Operação Pós-fixa: {operacao_pos_fixa}')
if __name__ == "__main__":
    main()