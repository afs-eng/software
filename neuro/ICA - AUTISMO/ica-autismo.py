# ICA / ABC – Inventário de Comportamentos Autísticos (57 itens)
# Correção por FACETAS (ES, RE, CO, LG, OS)
# Resposta: 1 = Verdadeiro | 0 = Falso
#
# PASSO A PASSO:
# 1) Pergunta os 57 itens (0/1)
# 2) Se resposta = 1, soma os pontos na FACETA correta (coluna do instrumento)
# 3) Calcula Subtotais (ES, RE, CO, LG, OS)
# 4) Calcula TOTAL GERAL e CLASSIFICAÇÃO

from dataclasses import dataclass
from typing import Dict, List


# =========================
# MODELO DE DADOS
# =========================
@dataclass
class ItemICA:
    numero: int
    texto: str
    faceta: str   # ES, RE, CO, LG, OS
    pontos: int   # pontos daquela linha na coluna da faceta


# =========================
# ITENS (57) + FACETA + PONTOS (conforme tabela do instrumento)
# =========================
ITENS_ICA: List[ItemICA] = [
    ItemICA(1,  "Gira em torno de si por longo período de tempo.", "CO", 4),
    ItemICA(2,  "Aprende uma tarefa, mas esquece rapidamente.", "OS", 2),
    ItemICA(3,  "É raro atender estímulo não-verbal social /ambiente (expressões, gesto situações).", "RE", 4),
    ItemICA(4,  "Ausência de resposta para solicitações verbais “venha cá”, “sente-se”.", "LG", 1),
    ItemICA(5,  "Usa brinquedos inapropriadamente.", "CO", 2),
    ItemICA(6,  "Pobre uso da discriminação visual (fixa uma característica objeto).", "ES", 2),
    ItemICA(7,  "Ausência do sorriso social.", "RE", 2),
    ItemICA(8,  "Uso inadequado de pronomes (eu por ele).", "LG", 3),
    ItemICA(9,  "Insiste em manter certos objetos consigo.", "CO", 3),
    ItemICA(10, "Parece não escutar (suspeita-se de perda de audição).", "ES", 3),
    ItemICA(11, "Fala monótona e sem ritmo.", "LG", 4),
    ItemICA(12, "Balança-se por longos períodos de tempo.", "CO", 4),
    ItemICA(13, "Não estende o braço para ser pego (nem o fez quando bebê).", "RE", 2),
    ItemICA(14, "Fortes reações frente a mudanças no ambiente.", "OS", 3),
    ItemICA(15, "Ausência de atenção ao seu nome quando entre 2 outras crianças.", "LG", 2),
    ItemICA(16, "Corre interrompendo com giros em torno de si, balanceio de mãos.", "CO", 4),
    ItemICA(17, "Ausência de resposta para expressão facial/sentimento de outros.", "RE", 3),
    ItemICA(18, "Raramente usa “sim” ou “eu”.", "LG", 2),
    ItemICA(19, "Possui habilidade numa área do desenvolvimento.", "OS", 4),
    ItemICA(20, "Ausência de respostas a solicitações verbal envolvendo o uso de referenciais de espaço.", "LG", 1),
    ItemICA(21, "Reação de sobressalto a som intenso (suspeita de surdez).", "ES", 3),
    ItemICA(22, "Balança as mãos.", "CO", 4),
    ItemICA(23, "Intensos acessos de raiva e/ou frequentes “chiliques”.", "OS", 3),
    ItemICA(24, "Evita ativamente o contato visual.", "RE", 4),
    ItemICA(25, "Resiste ao toque / ao ser pego / ao carinho.", "RE", 4),

    ItemICA(26, "Não reage a estímulos dolorosos.", "ES", 3),
    ItemICA(27, "Difícil e rígido no colo (ou foi quando bebê).", "RE", 3),
    ItemICA(28, "Flácido quando no colo.", "RE", 2),
    ItemICA(29, "Aponta para indicar objeto desejado.", "LG", 2),
    ItemICA(30, "Anda nas pontas dos pés.", "CO", 2),
    ItemICA(31, "Machuca outros mordendo, batendo, etc.", "OS", 2),
    ItemICA(32, "Repete a mesma frase muitas vezes.", "LG", 3),
    ItemICA(33, "Ausência de imitação de brincadeiras de outras crianças.", "RE", 3),
    ItemICA(34, "Ausência de reação do piscar quando luz forte incide em seus olhos.", "ES", 1),
    ItemICA(35, "Machuca-se mordendo, batendo a cabeça, etc.", "CO", 2),
    ItemICA(36, "Não espera para ser atendido (quer as coisas imediatamente).", "OS", 2),
    ItemICA(37, "Não aponta para mais que cinco objetos.", "LG", 1),
    ItemICA(38, "Dificuldade de fazer amigos.", "RE", 4),
    ItemICA(39, "Tapa as orelhas para vários sons.", "ES", 4),
    ItemICA(40, "Gira, bate objetos muitas vezes.", "CO", 4),
    ItemICA(41, "Dificuldades para o treino de toalete.", "OS", 1),
    ItemICA(42, "Usa de 0 a 5 palavras/dia para indicar necessidade e o que quer.", "LG", 2),
    ItemICA(43, "Frequentemente muito ansioso ou medroso.", "RE", 3),
    ItemICA(44, "Franze, cobre ou vira os olhos quando em presença de luz natural.", "ES", 3),
    ItemICA(45, "Não se veste sem ajuda.", "OS", 1),
    ItemICA(46, "Repete constantemente as mesmas palavras e/ou sons.", "LG", 3),
    ItemICA(47, "“Olha através” das pessoas.", "RE", 4),
    ItemICA(48, "Repete perguntas e frases ditas por outras pessoas.", "LG", 4),
    ItemICA(49, "Frequentemente inconsciente dos perigos de situações do ambiente.", "OS", 2),
    ItemICA(50, "Prefere manipular e ocupar-se com objetos inanimados.", "OS", 4),
    ItemICA(51, "Toca, cheira ou lambe objetos do ambiente.", "CO", 3),
    ItemICA(52, "Frequentemente não reage visualmente à presença de novas pessoas.", "ES", 3),
    ItemICA(53, "Repete sequências de comportamentos complicados (cobrir coisas, por ex.).", "CO", 4),
    ItemICA(54, "Destrutivo com seus brinquedos e coisas da família.", "CO", 2),
    ItemICA(55, "O atraso no desenvolvimento identificado antes dos 30 meses.", "OS", 1),
    ItemICA(56, "Usa mais que 15 e menos que 30 frases diárias para comunicar-se.", "LG", 3),
    ItemICA(57, "Olha fixamente o ambiente por longos períodos de tempo.", "ES", 4),
]


# =========================
# CLASSIFICAÇÃO FINAL (TOTAL GERAL)
# =========================
def classificar_total_geral(total: int) -> str:
    # conforme tabela do instrumento
    if total < 47:
        return "Não Clínico"
    elif 47 <= total <= 53:
        return "Leve probabilidade para autismo"
    elif 54 <= total <= 67:
        return "Moderada probabilidade para autismo"
    else:  # >= 68
        return "Clínico - Autismo"


# =========================
# APLICAÇÃO INTERATIVA
# =========================
def aplicar_ica() -> Dict:
    print("\n=== ICA / ABC – Inventário de Comportamentos Autísticos (57 itens) ===")
    print("Responda: 1 = Verdadeiro | 0 = Falso\n")
    print("Obs.: Quando marcar 1, o sistema soma os pontos NA FACETA correspondente (ES, RE, CO, LG, OS).\n")

    subtotais = {"ES": 0, "RE": 0, "CO": 0, "LG": 0, "OS": 0}
    respostas = {}  # guarda 0/1 por item

    for item in ITENS_ICA:
        while True:
            resp = input(f"[{item.numero:02d}] {item.texto} (1/0): ").strip()
            if resp not in {"0", "1"}:
                print("Entrada inválida. Digite somente 1 (verdadeiro) ou 0 (falso).")
                continue

            resp_int = int(resp)
            respostas[item.numero] = resp_int

            if resp_int == 1:
                subtotais[item.faceta] += item.pontos

            break

    total_geral = sum(subtotais.values())
    classificacao = classificar_total_geral(total_geral)

    print("\n==== RESULTADOS (PONTOS BRUTOS) ====")
    print(f"ES (Estímulo Sensorial): {subtotais['ES']}")
    print(f"RE (Relacionamento):     {subtotais['RE']}")
    print(f"CO (Corpo e Objeto):     {subtotais['CO']}")
    print(f"LG (Linguagem):          {subtotais['LG']}")
    print(f"OS (Pessoal/Social):     {subtotais['OS']}")

    print("\nTOTAL GERAL:", total_geral)
    print("CLASSIFICAÇÃO:", classificacao)

    return {
        "subtotais": subtotais,
        "total_geral": total_geral,
        "classificacao": classificacao,
        "respostas": respostas,
    }


if __name__ == "__main__":
    aplicar_ica()
