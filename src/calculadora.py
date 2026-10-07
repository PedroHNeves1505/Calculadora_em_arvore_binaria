from tokenizador import tokenizar_expressao
import time
import os
import subprocess

def obter_expressao_e_tokens():
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