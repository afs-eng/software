"""
10 exercícios de dicionários

1 - Contar letras: leia uma string e crie um dicionário com a contagem de cada letra.

2 - Contar palavras: leia uma frase e conte quantas vezes cada palavra aparece.

3 - Inverter chave/valor: dado um dicionário {chave: valor}, gere outro {valor: chave} (assuma valores únicos).

4 - Buscar aluno: crie um dicionário nome -> nota. Pergunte um nome e mostre a nota (ou “não encontrado”).

5 - Maior valor: encontre a chave com o maior valor em um dicionário (sem usar max() diretamente no dicionário).

6 - Mesclar dicionários: junte dois dicionários. Se a chave repetir, some os valores.

7 - Agrupar por inicial: dada uma lista de nomes, crie um dicionário onde a chave é a letra inicial e o valor é uma lista de nomes com aquela inicial.

8 - Filtro por valor: dado um dicionário e um número x, crie um novo dicionário apenas com pares cujo valor seja maior que x.

9 - Agenda de contatos: faça um menu simples para: adicionar contato, remover, listar e buscar (telefone/email como valores).

10 - Dicionário aninhado: armazene produtos com {nome: {"preco": ..., "estoque": ...}} e crie funções para:

listar produtos

calcular valor total do estoque

atualizar estoque de um produto

"""
from traceback import print_tb

# ======================================================================================================================
""" 
# 1 - Contar letras: leia uma string e crie um dicionário com a contagem de cada letra.

str = 'junte dois dicionários. Se a chave repetir, some os valores'

letras = str.split()
d = {}

for letra in letras:
    d[letra] = d.get(letra, len(letra))

# print(d)

#=======================================================================================================================

# 2 - Contar palavras: leia uma frase e conte quantas vezes cada palavra aparece.

s = 'Maior valor: encontre a chave com o maior valor em um dicionário (sem usar max() diretamente no dicionário).'

# Remove pontuações e converte para minúsculas para contar corretamente
s = s.replace('(', '').replace(')', '').replace('.', '').replace(':', '')
ss = s.lower().split()

contagem = {}

for palavra in ss:
    contagem[palavra] = contagem.get(palavra, 0) + 1


print(f"Frase original: {s}")
print("Contagem de palavras:")
print(contagem)


#=======================================================================================================================
# 3 - Inverter chave/valor: dado um dicionário {chave: valor}, gere outro {valor: chave} (assuma valores únicos).


dic = {'valor1': 1, 'valor2': 2, 'valor3': 3, 'valor4': 4}
novo_dic = {}
for chave, valor in dic.items():
    novo_dic[valor] = novo_dic.get(valor, chave)
# print(novo_dic)

#=======================================================================================================================



# 4 - Buscar aluno: crie um dicionário nome -> nota. Pergunte um nome e mostre a nota (ou “não encontrado”).

aluno = {'andre':8, 'jacqueline': 9, 'camila': 10, 'gaby': 9}

nome = input('Digite seu nome: ')
if nome in aluno:
    print(f'Nome: {nome}\nNota: {aluno[nome]}')
else:
    print('Aluno não encontrado')

#=======================================================================================================================
# 5 - Maior valor: encontre a chave com o maior valor em um dicionário (sem usar max() diretamente no dicionário).

valores  = {'valor1': 46, 'valor2': 21, 'valor3': 34, 'valor4': 43}

maior_chave = None
maior_valor = None

for chave, valor in valores.items():
    if maior_valor is None or valor > maior_valor:
        maior_valor = valor
        maior_chave = chave

print(f'{maior_chave}:{maior_valor}')
#=======================================================================================================================

#=======================================================================================================================

#=======================================================================================================================

#=======================================================================================================================
"""

# 6 - Mesclar dicionários: junte dois dicionários. Se a chave repetir, some os valores.


valores1  = {'valor1': 46, 'valor2': 21, 'valor3': 34, 'valor4': 50}

valores2 = {'valor5': 33, 'valor6': 21, 'valor7': 39, 'valor4': 11}
# {'valor1': 46, 'valor2': 21, 'valor3': 34, 'valor4': 22, 'valor5': 33, 'valor6': 21, 'valor7': 39}

aux = valores1.copy()

for chave, valor in valores2.items():
    if chave in aux:
        aux[chave] += valor
    else:
        aux[chave] = valor


valores = {'CB': 12, 'SM': 12, 'DG': 5, 'CN': 13, 'CD': 9, 'VC': 13, 'SNL': 9, 'RM': 14, 'CO': 12, 'PS': 11}


cv = []

for chave, valor in valores.items():
    if 'SM' in chave:
        sm = valor
        cv.append(sm)
    elif 'VC' in chave:
        vc= valor
        cv.append(vc)
    elif 'CO' in chave:
        co= valor
        cv.append(co)

total = sum(cv)
print(f'Total: {total}')

































