# Sistema de correção do EBADEP-IJ em Python

# Itens com correção normal (0/1/2)
itens_branco = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 20, 21, 22, 24, 26, 27]

# Itens com correção invertida (2/1/0)
itens_azul = [9, 12, 13, 14, 15, 16, 17, 18, 19, 23, 25]

# Lista para armazenar as respostas do usuário
respostas = []

print("==== Sistema de Correção EBADEP-IJ ====")
print("Digite sua resposta para cada item (0, 1 ou 2):\n")

# Coleta das respostas
for i in range(1, 46):
    while True:
        try:
            resp = int(input(f"Item {i}: "))
            if resp in [0, 1, 2]:
                respostas.append(resp)
                break
            else:
                print("⚠️ Resposta inválida. Digite apenas 0, 1 ou 2.")
        except ValueError:
            print("⚠️ Entrada inválida. Digite apenas números inteiros 0, 1 ou 2.")

# Correção das respostas
pontuacoes_corrigidas = []
for i in range(1, 46):
    original = respostas[i-1]
    if i in itens_azul:
        corrigido = 2 - original  # inversão
    else:
        corrigido = original
    pontuacoes_corrigidas.append(corrigido)

# Cálculo da pontuação total
pontuacao_total = sum(pontuacoes_corrigidas)

# Classificação simples da pontuação
if pontuacao_total <= 30:
    classificacao = "Baixa"
elif pontuacao_total <= 60:
    classificacao = "Média"
else:
    classificacao = "Alta"

# Resultado final
print("\n==== RESULTADO FINAL ====")
print(f"Pontuação Total Corrigida: {pontuacao_total}")
print(f"Classificação: {classificacao}")

# (Opcional) Mostrar pontuações item a item
print("\n==== Pontuação por Item ====")
for i in range(45):
    tipo = "2/1/0" if (i+1) in itens_azul else "0/1/2"
    print(f"Item {i+1:2d}: Resposta = {respostas[i]}, Tipo = {tipo}, Corrigido = {pontuacoes_corrigidas[i]}")
