from tokenizador import tokenizar_expressao
import time
import os
import subprocess

def obter_expressao():
    while True:
        print('Digite a expressão a ser resolvida')
        expressao = input('--> ')
        
        if expressao or expressao.strip():
            return expressao
        
        print('A expressão está vazia!')
        time.sleep(3)
        subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)