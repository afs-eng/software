# ------------------------------
# SISTEMA BPQ - versão corrigida
# Respostas: 1 (verdadeiro) ou 0 (falso)
# Itens com *: se resposta = 0 → 1 ponto
# ------------------------------

subescalas = {
    "Impulsividade":      [1, 10, 26, 34, 42, 57, 64, 68, 71],
    "Instabilidade afetiva": [2, 11, 19, 27, 35, 43, 49, 58, 65, 72],
    "Abandono":           [3, 12, 20, 28, 44, 50, 59, 66, 73, 78],
    "Relacionamentos":    [4, 13, 21, 29, 36, 45, 51, 60],
    "Autoimagem":         [5, 14, 37, 46, 52, 61, 67, 70, 74],
    "Suicídio / Automutilação": [6, 15, 22, 30, 38, 53, 75],
    "Vazio":              [7, 16, 23, 31, 39, 54, 62, 69, 76, 79],
    "Raiva intensa":      [8, 17, 24, 32, 40, 47, 55, 63, 77, 80],
    "Estados quase psicóticos": [9, 18, 25, 33, 41, 48, 56],
}

# Itens com pontuação invertida (*)
itens_invertidos = {10, 28, 4, 45, 60, 52, 67, 53, 54, 8, 32, 48}

# Classificação por subescala
classificacoes = {
    "Impulsividade": [(0,2,"Não clínico"), (3,4,"Leve"), (5,6,"Moderado"), (7,9,"Grave")],
    "Instabilidade afetiva": [(0,2,"Não clínico"), (3,5,"Leve"), (6,8,"Moderado"), (9,10,"Grave")],
    "Abandono": [(0,2,"Não clínico"), (3,5,"Leve"), (6,8,"Moderado"), (9,10,"Grave")],
    "Relacionamentos": [(0,1,"Não clínico"), (2,3,"Leve"), (4,5,"Moderado"), (6,8,"Grave")],
    "Autoimagem": [(0,2,"Não clínico"), (3,4,"Leve"), (5,6,"Moderado"), (7,9,"Grave")],
    "Suicídio / Automutilação": [(0,1,"Não clínico"), (2,3,"Leve"), (4,5,"Moderado"), (6,7,"Grave")],
    "Vazio": [(0,2,"Não clínico"), (3,5,"Leve"), (6,8,"Moderado"), (9,10,"Grave")],
    "Raiva intensa": [(0,2,"Não clínico"), (3,5,"Leve"), (6,8,"Moderado"), (9,10,"Grave")],
    "Estados quase psicóticos": [(0,1,"Não clínico"), (2,3,"Leve"), (4,5,"Moderado"), (6,7,"Grave")],
}

bpq_geral = [
    (0,29,"Não clínico"),
    (30,34,"Leve"),
    (35,42,"Moderado"),
    (43,80,"Grave")
]

# ------------------------------

respostas = {}

print("\n=== BPQ - Digite 1 (verdadeiro) ou 0 (falso) ===\n")

for item in range(1, 81):
    while True:
        resp = input(f"Item {item}: ")
        if resp in ["1", "0"]:
            respostas[item] = int(resp)
            break
        else:
            print("Digite apenas 1 ou 0.")

resultados = {}
pontuacao_total = 0

for nome, itens in subescalas.items():
    soma = 0
    for item in itens:
        resposta = respostas[item]

        # regra atual:
        if item in itens_invertidos:
            ponto = 1 if resposta == 0 else 0
        else:
            ponto = resposta  # 1 = 1 ponto, 0 = 0 pontos

        soma += ponto

    resultados[nome] = soma
    pontuacao_total += soma

print("\n=== RESULTADOS ===\n")

for nome, valor in resultados.items():
    nivel = next(label for (minv,maxv,label) in classificacoes[nome] if minv <= valor <= maxv)
    print(f"{nome}: {valor} pontos → {nivel}")

nivel_geral = next(label for (minv,maxv,label) in bpq_geral if minv <= pontuacao_total <= maxv)

print(f"\nPontuação total: {pontuacao_total}")
print(f"Classificação geral: {nivel_geral}")
