# Calculadora de Expressões Matemáticas com Árvores Binárias

Este projeto consiste numa calculadora modularizada em **Python** que processa expressões matemáticas infixas, valida tokens, converte para notação pós-fixa (*Shunting Yard*), constrói uma **Árvore de Expressão Binária** e realiza cálculos recursivos, além de gerar os percursos da árvore e reconstruir a expressão original.

---

## 🚀 Funcionalidades

* **Tokenização e Validação:** Lê a expressão do utilizador, remove espaços e valida caracteres suportados.
* **Conversão Infixa para Pós-fixa:** Utiliza o algoritmo *Shunting Yard* para respeitar a precedência dos operadores.
* **Construção da Árvore Binária:** Cria uma estrutura de nós (`No`) representativa da expressão matemática.
* **Cálculo Recursivo:** Avalia o valor final da expressão percorrendo a árvore de forma recursiva.
* **Tratamento de Erros:** Deteção segura de divisão por zero com reinício automático do programa.
* **Percursos da Árvore:** Gera os percursos em **Pré-ordem**, **Em ordem** (In-order) e **Pós-ordem**.
* **Reconstrução da Expressão:** Recria a expressão infixa a partir da árvore com os parênteses corretos.
* **Testes Automatizados:** Script de testes validando cenários e expressões complexas.

---

## 📂 Estrutura do Projeto

```text
Calculadora_em_arvore_binaria/
│
├── src/
│   ├── __init__.py
│   ├── __main__.py          # Ponto de entrada principal da aplicação
│   ├── arvore.py            # Lógica de construção da árvore binária
│   ├── calculadora.py       # Funções de cálculo, reconstrução e percursos
│   ├── conversor.py         # Conversão para notação pós-fixa
│   ├── no.py                # Definição da classe No da árvore
│   └── tokenizador.py       # Validação e tokenização da expressão
│
├── test/
│   ├── __init__.py
│   └── tests_calculadora.py # Testes automatizados do sistema
│
├── .gitignore
└── README.md
```

---

## 🛠️ Tecnologias Utilizadas

* Python 3.11+
* Pytest (para os testes automatizados)

---

## ⚙️ Como Executar o Projeto

1. Certifica-te de que tens o Python instalado no teu computador.

2. Abre o terminal na raiz do projeto (Calculadora_em_arvore_binaria).

3. Executa a aplicação utilizando o módulo principal:

```bash
python -m src
```

---

## 🧪 Como Executar os Testes

1. Na raiz do projeto, executa o comando de testes:

```bash
python test/tests_calculadora.py  
```

---

## 💡 Exemplo de Utilização

Ao iniciar o programa, podes inserir expressões como:

```plaintext
Digite a expressão a ser resolvida
--> ((20 / 5) + 3) * (9 - (2 + 1))
```

O sistema devolverá os tokens, a notação pós-fixa, os percursos da árvore e o resultado final computado!

---

## Perguntas Respondidas

1. Por que a expressão precisa ser tokenizada?<br>
R: A expressão precisa de ser tokenizada para transformar a string de texto bruto numa lista de unidades significativas e isoladas (como números com vários dígitos, decimais e operadores), facilitando o tratamento e o processamento lógico subsequente.

2. Por que uma pilha é adequada para operadores e parênteses?<br>
R: Uma pilha é adequada porque o seu comportamento LIFO (último a entrar, primeiro a sair) lida de forma natural com a gestão de precedência dos operadores e o comportamento aninhado dos parênteses.

3. Por que o primeiro pop na construção da árvore corresponde ao filho direito?<br>
R: Porque, na notação pós-fixa, os operandos aparecem por ordem de avaliação inversa, fazendo com que o elemento retirado primeiro do topo da pilha corresponda estruturalmente ao operando localizado à direita do operador.

4. Qual a relação entre pós-ordem e notação pós-fixa?<br>
R: O percurso em pós-ordem (esquerda, direita, raiz) numa árvore de expressão gera exatamente a sequência da notação pós-fixa (ou polaca inversa) da expressão matemática correspondente.

5. Para uma árvore com n nós, qual a complexidade de tempo para calcular toda a expressão? Justifique.<br>
R: A complexidade de tempo é linear, ou seja, O(n), pois a avaliação recursiva visita cada um dos $n$ nós da árvore exatamente uma vez para computar o resultado.

6. O que determina a quantidade máxima de chamadas recursivas simultâneas?<br>
R: A quantidade máxima de chamadas recursivas simultâneas é determinada pela altura (ou profundidade máxima) da árvore, pois a pilha de execução do sistema armazena uma chamada por cada nível percorrido até ao nó mais profundo, sendo também condicionada pelo limite de recursão imposto pelo ambiente de execução.

---

## Integrante

Nome: Pedro Henrique Neves<br>
RM: 571382
