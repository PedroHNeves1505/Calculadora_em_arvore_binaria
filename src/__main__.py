from calculadora import obter_expressao
from tokenizador import tokenizar_expressao

def main():
    expressao = obter_expressao()
    tokenizar_expressao(expressao)

if __name__ == "__main__":
    main()