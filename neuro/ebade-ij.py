# Sistema completo de correção do EBADEP-IJ (com explicações)

# Lista dos itens com correção normal
itens_branco = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 20, 21, 22, 24, 26, 27]

# Lista dos itens com correção invertida (resposta corrigida = 2 - resposta)
itens_azul = [9, 12, 13, 14, 15, 16, 17, 18, 19, 23, 25]

# Lista para armazenar as respostas do usuário
respostas = []

print("==== SISTEMA DE CORREÇÃO EBADEP-IJ ====\n")
print("Responda aos 45 itens com 0, 1 ou 2\n")

# Coleta das respostas com validação
for i in range(1, 46):
    while True:
        try:
            resposta = int(input(f"Item {i:02d}: "))
            if resposta in [0, 1, 2]:
                respostas.append(resposta)
                break
            else:
                print("⚠️ Digite apenas 0, 1 ou 2.")
        except ValueError:
            print("⚠️ Entrada inválida. Digite apenas números inteiros 0, 1 ou 2.")

# Lista para armazenar as pontuações corrigidas
pontuacoes_corrigidas = []

# Aplicar a correção item a item
for i in range(1, 46):
    original = respostas[i - 1]  # Acessa o item na posição correta (índice começa em 0)

    # Se o item for da lista azul, invertemos a pontuação
    if i in itens_azul:
        corrigido = 2 - original
    else:
        corrigido = original

    pontuacoes_corrigidas.append(corrigido)

# Soma total da pontuação corrigida
pontuacao_total = sum(pontuacoes_corrigidas)

# Classificação baseada em faixas arbitrárias (pode ser ajustada conforme critérios clínicos)
if pontuacao_total <= 30:
    classificacao = "Baixa"
elif pontuacao_total <= 60:
    classificacao = "Média"
else:
    classificacao = "Alta"

# Exibir os resultados
print("\n==== RESULTADO FINAL ====")
print(f"Pontuação Total Corrigida: {pontuacao_total}")
print(f"Classificação: {classificacao}")

# Detalhamento por item (opcional para debug)
print("\n==== PONTUAÇÃO ITEM A ITEM ====")
for i in range(45):
    tipo = "2/1/0" if (i + 1) in itens_azul else "0/1/2"
    print(f"Item {i + 1:02d}: Resposta = {respostas[i]}, Tipo = {tipo}, Corrigido = {pontuacoes_corrigidas[i]}")
