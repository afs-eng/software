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















































































