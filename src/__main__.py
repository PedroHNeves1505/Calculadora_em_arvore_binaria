from calculadora import obter_expressao_e_tokens

def main():
    expressao, tokens = obter_expressao_e_tokens()
    print(f'Expressao: {expressao} | Token: {tokens}')

if __name__ == "__main__":
    main()