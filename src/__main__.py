from calculadora import obter_expressao_e_tokens, gerar_expressao, calcular, pre_ordem, em_ordem, pos_ordem
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
            
        percurso_pre = pre_ordem(arvore)
        percurso_em = em_ordem(arvore)
        percurso_pos = pos_ordem(arvore)
        
        print("\n--- Resultado ---")
        print(f"Expressão: {expressao}")
        print(f"Tokens: {tokens}")
        print(f"Pós-fixa (Shunting Yard): {operacao_pos_fixa}")
        print(f"Árvore: {arvore}")
        print(f"Reconstruída: {expressao_reconstruida}")
        print(f"Pré-ordem (Raiz, Esq, Dir): {percurso_pre}")
        print(f"Em ordem (Esq, Raiz, Dir): {percurso_em}")
        print(f"Pós-ordem (Esq, Dir, Raiz): {percurso_pos}")
        print(f"Resultado Final: {resultado}\n")
        break


if __name__ == "__main__":
    main()