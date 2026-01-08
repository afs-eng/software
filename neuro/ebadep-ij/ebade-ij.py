# ==========================================
# EBADEP-IJ (27 itens) — Correção completa
# Baseado no manual anexado
# ==========================================

from typing import List, Dict, Tuple, Union

# Itens com semântica negativa (pontuação direta: 0/1/2)
ITENS_NEGATIVOS = {
    1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 20, 21, 22, 24, 26, 27
}

# Itens com semântica positiva (pontuação invertida: 2/1/0 => corrigido = 2 - resposta)
ITENS_POSITIVOS = {
    9, 12, 13, 14, 15, 16, 17, 18, 19, 23, 25
}

# Tabela (Amostra Geral): Escore -> (Percentil, T, Estanino)
# Transcrita das tabelas do manual (págs. 14–15)
# Observação: percentil pode ser "<1" ou ">99"
TABELA_AMOSTRA_GERAL: Dict[int, Tuple[Union[int, str], int, int]] = {
    0: ("<1", 19, 1),
    1: ("<1", 20, 1),
    2: (4, 21, 1),
    3: (4, 22, 1),
    4: (4, 23, 1),
    5: (4, 24, 1),
    6: (4, 25, 1),
    7: (4, 26, 1),
    8: (4, 27, 1),
    9: (4, 28, 1),
    10: (4, 29, 1),
    11: (5, 30, 1),
    12: (5, 31, 1),
    13: (5, 32, 1),
    14: (5, 33, 1),
    15: (6, 34, 1),
    16: (6, 35, 2),
    17: (7, 36, 2),
    18: (7, 37, 2),
    19: (8, 38, 2),
    20: (10, 39, 2),
    21: (11, 40, 3),
    22: (13, 41, 3),
    23: (15, 42, 3),
    24: (18, 43, 3),
    25: (21, 44, 3),
    26: (25, 45, 4),
    27: (29, 46, 4),
    28: (35, 47, 4),
    29: (41, 48, 4),
    30: (48, 49, 4),
    31: (55, 50, 5),
    32: (63, 51, 5),
    33: (69, 52, 5),
    34: (74, 53, 5),
    35: (78, 54, 5),
    36: (81, 55, 6),
    37: (83, 56, 6),
    38: (85, 57, 6),
    39: (86, 58, 6),
    40: (87, 60, 6),
    41: (88, 61, 7),
    42: (89, 62, 7),
    43: (90, 63, 7),
    44: (91, 64, 7),
    45: (92, 65, 7),
    46: (93, 66, 8),
    47: (94, 67, 8),
    48: (95, 68, 8),
    49: (96, 69, 8),
    50: (97, 70, 8),
    51: (98, 71, 9),
    52: (99, 72, 9),
    53: (99, 73, 9),
    54: (">99", 74, 9),
}

def classificar_tabela_18(pontuacao_total: int) -> str:
    """
    Classificação conforme a Tabela 18 (Amostra Geral):
    0–15: Comportamento positivo 1
    16–20: Comportamento positivo 2
    21–30: Com sintomatologia leve
    31–45: Com sintomatologia moderada
    46–54: Com sintomatologia grave ou severa
    """
    if 0 <= pontuacao_total <= 15:
        return "Comportamento positivo 1"
    if 16 <= pontuacao_total <= 20:
        return "Comportamento positivo 2"
    if 21 <= pontuacao_total <= 30:
        return "Com sintomatologia leve"
    if 31 <= pontuacao_total <= 45:
        return "Com sintomatologia moderada"
    if 46 <= pontuacao_total <= 54:
        return "Com sintomatologia grave ou severa"
    return "Pontuação fora do intervalo esperado (0–54). Verifique as respostas."

def corrigir_item(item: int, resposta: int) -> int:
    """
    Resposta deve ser 0, 1 ou 2 (conforme marcação do examinando).
    - Itens negativos: corrigido = resposta
    - Itens positivos: corrigido = 2 - resposta (inversão)
    """
    if item in ITENS_POSITIVOS:
        return 2 - resposta
    return resposta

def avaliar_ebadep_ij(respostas: List[int], detalhar: bool = True) -> Dict[str, object]:
    """
    Recebe lista com 27 respostas (0/1/2), na ordem dos itens 1..27.
    Retorna dicionário com somas, total, classificação e (se disponível) percentil/T/estanino.
    """
    if len(respostas) != 27:
        raise ValueError("É obrigatório fornecer exatamente 27 respostas (itens 1 a 27).")

    # validação de valores
    for i, r in enumerate(respostas, start=1):
        if r not in (0, 1, 2):
            raise ValueError(f"Resposta inválida no item {i}: {r}. Use apenas 0, 1 ou 2.")

    pontuacoes_corrigidas = []
    soma_negativos = 0
    soma_positivos = 0

    for item in range(1, 28):
        original = respostas[item - 1]
        corrigido = corrigir_item(item, original)
        pontuacoes_corrigidas.append(corrigido)

        if item in ITENS_POSITIVOS:
            soma_positivos += corrigido
        else:
            soma_negativos += corrigido

    pontuacao_total = soma_negativos + soma_positivos
    classificacao = classificar_tabela_18(pontuacao_total)

    # Normas amostra geral (percentil/T/estanino) — quando pontuação dentro de 0..54
    normas = TABELA_AMOSTRA_GERAL.get(pontuacao_total)

    resultado = {
        "soma_itens_negativos": soma_negativos,
        "soma_itens_positivos": soma_positivos,
        "pontuacao_total": pontuacao_total,
        "classificacao_tabela_18": classificacao,
        "normas_amostra_geral": None if normas is None else {
            "percentil": normas[0],
            "T": normas[1],
            "estanino": normas[2],
        },
    }

    if detalhar:
        resultado["detalhe_itens"] = [
            {
                "item": item,
                "resposta": respostas[item - 1],
                "invertido": (item in ITENS_POSITIVOS),
                "corrigido": pontuacoes_corrigidas[item - 1],
            }
            for item in range(1, 28)
        ]

    return resultado

def coletar_respostas_interativas() -> List[int]:
    print("==== EBADEP-IJ — Correção (27 itens) ====\n")
    print("Digite a alternativa marcada em cada item como 0, 1 ou 2.")
    print("0 = Nunca/Poucas vezes | 1 = Algumas vezes | 2 = Muitas vezes/Sempre\n")

    respostas: List[int] = []
    for item in range(1, 28):
        while True:
            try:
                r = int(input(f"Item {item:02d}: ").strip())
                if r in (0, 1, 2):
                    respostas.append(r)
                    break
                print("Entrada inválida. Use apenas 0, 1 ou 2.")
            except ValueError:
                print("Entrada inválida. Use apenas números inteiros: 0, 1 ou 2.")
    return respostas

def imprimir_resultado(resultado: Dict[str, object], mostrar_detalhes: bool = False) -> None:
    print("\n==== RESULTADO FINAL ====")
    print(f"Soma (itens negativos): {resultado['soma_itens_negativos']}")
    print(f"Soma (itens positivos): {resultado['soma_itens_positivos']}")
    print(f"Pontuação Total (score bruto): {resultado['pontuacao_total']}")
    print(f"Classificação (Tabela 18): {resultado['classificacao_tabela_18']}")

    normas = resultado.get("normas_amostra_geral")
    if normas:
        print("\n==== NORMAS (AMOSTRA GERAL) ====")
        print(f"Percentil: {normas['percentil']}")
        print(f"Escore T: {normas['T']}")
        print(f"Estanino: {normas['estanino']}")

    if mostrar_detalhes and "detalhe_itens" in resultado:
        print("\n==== DETALHE ITEM A ITEM ====")
        for d in resultado["detalhe_itens"]:
            inv = "Sim" if d["invertido"] else "Não"
            print(f"Item {d['item']:02d}: resposta={d['resposta']} | invertido={inv} | corrigido={d['corrigido']}")

if __name__ == "__main__":
    # Modo 1: interativo (digitando item a item)
    respostas = coletar_respostas_interativas()

    # Se quiser rodar SEM detalhamento no retorno, troque detalhar=False
    resultado = avaliar_ebadep_ij(respostas, detalhar=True)

    # Mostrar ou não o detalhe item-a-item
    imprimir_resultado(resultado, mostrar_detalhes=False)
