from calculadora import obter_expressao_e_tokens, gerar_expressao, calcular
from conversor import conversor_posfixa
from arvore import construir_arvore
import time
import os
import subprocess

def main():
    while True:    
        expressao, tokens = obter_expressao_e_tokens()
        operacao_pos_fixa = conversor_posfixa(tokens)
        arvore = construir_arvore(operacao_pos_fixa)
        expressao_reconstruida = gerar_expressao(arvore)
        
        resultado = calcular(arvore)
        
        if resultado == 'reiniciar':
            print("\nErro: Divisão por zero detetada! A reiniciar o programa...")
            time.sleep(3)
            subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
            continue
        
        print("\n--- Resultado ---")
        print(f"Expressão: {expressao}")
        print(f"Tokens: {tokens}")
        print(f"Pós-fixa: {operacao_pos_fixa}")
        print(f"Árvore: {arvore}")
        print(f"Reconstruída: {expressao_reconstruida}")
        print(f"Resultado Final: {resultado}\n")


if __name__ == "__main__":
    main()