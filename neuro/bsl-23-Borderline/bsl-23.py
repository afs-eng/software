# bsl23_system.py
# Sistema de correção do BSL-23 (versão brasileira) + módulo complementar
# Referência do instrumento: BSL-23 - Nova versão brasileira (Technical Report, 2021)  :contentReference[oaicite:2]{index=2}

from dataclasses import dataclass
from typing import List, Optional


# =========================
# CONFIGURAÇÕES BSL-23
# =========================
BSL23_N_ITEMS = 23
BSL23_MIN = 0
BSL23_MAX = 4

RESP_LABELS_BSL23 = {
    0: "Nem um pouco",
    1: "Um pouco",
    2: "Consideravelmente",
    3: "Muito",
    4: "Muito fortemente",
}

# Classificação conforme quadro de correção do instrumento :contentReference[oaicite:3]{index=3}
# Observação: pontos de corte com intervalos contínuos.
BSL23_CUTS = [
    ("Nenhum ou baixo", 0.0, 0.3),
    ("Suave", 0.3, 0.7),
    ("Moderado", 0.7, 1.7),
    ("Alto", 1.7, 2.7),
    ("Muito alto", 2.7, 3.5),
    ("Extremamente alto", 3.5, 4.0),
]


# =========================
# CONFIGURAÇÕES BSL Complementar (11 itens)
# =========================
BSL_COMP_N_ITEMS = 11
BSL_COMP_MIN = 0
BSL_COMP_MAX = 4

RESP_LABELS_COMP = {
    0: "Nenhuma vez",
    1: "Uma vez",
    2: "2 a 3 vezes",
    3: "4 a 6 vezes",
    4: "Diariamente / com muita frequência",
}


# =========================
# MODELOS DE DADOS
# =========================
@dataclass
class BSL23Result:
    respostas: List[int]
    soma: int
    media: float
    classificacao: str
    qualidade_vida_percent: Optional[int] = None


@dataclass
class BSLComplementarResult:
    respostas: List[int]
    soma: int
    media: float


# =========================
# FUNÇÕES AUXILIARES
# =========================
def _input_int_range(prompt: str, min_v: int, max_v: int) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
            if val < min_v or val > max_v:
                raise ValueError
            return val
        except ValueError:
            print(f"Entrada inválida. Digite um número inteiro entre {min_v} e {max_v}.")


def _input_yes_no(prompt: str) -> bool:
    while True:
        raw = input(prompt).strip().lower()
        if raw in ("s", "sim", "y", "yes"):
            return True
        if raw in ("n", "nao", "não", "no"):
            return False
        print("Resposta inválida. Digite 's' (sim) ou 'n' (não).")


def classificar_bsl23(media: float) -> str:
    # Regra prática: fecha o topo em 4.0 por segurança numérica.
    media = max(0.0, min(4.0, media))

    for nome, a, b in BSL23_CUTS:
        # Intervalos [a, b) e último fecha em [3.5, 4.0]
        if nome != "Extremamente alto":
            if a <= media < b:
                return nome
        else:
            if a <= media <= b:
                return nome

    # fallback (não deveria ocorrer)
    return "Indefinido"


# =========================
# APLICAÇÃO PRINCIPAL
# =========================
def aplicar_bsl23() -> BSL23Result:
    print("\n=== BSL-23 (Escala principal) ===")
    print("Responda cada item com um número de 0 a 4, conforme a escala:")
    for k in range(0, 5):
        print(f"  {k} = {RESP_LABELS_BSL23[k]}")
    print("\nImportante: acompanhe os itens pelo formulário impresso/PDF (itens 1 a 23).")

    respostas: List[int] = []
    for i in range(1, BSL23_N_ITEMS + 1):
        val = _input_int_range(f"Item {i:02d} (0-4): ", BSL23_MIN, BSL23_MAX)
        respostas.append(val)

    soma = sum(respostas)
    media = soma / BSL23_N_ITEMS
    classificacao = classificar_bsl23(media)

    # Qualidade de vida (opcional)
    qualidade = None
    if _input_yes_no("\nDeseja registrar a qualidade de vida geral (0 a 100%)? (s/n): "):
        qualidade = _input_int_range("Qualidade de vida (0-100): ", 0, 100)

    return BSL23Result(
        respostas=respostas,
        soma=soma,
        media=media,
        classificacao=classificacao,
        qualidade_vida_percent=qualidade,
    )


def aplicar_bsl_complementar() -> BSLComplementarResult:
    print("\n=== BSL Complementar (Comportamentos) ===")
    print("Responda cada item com um número de 0 a 4, conforme a escala:")
    for k in range(0, 5):
        print(f"  {k} = {RESP_LABELS_COMP[k]}")
    print("\nImportante: acompanhe os itens pelo formulário impresso/PDF (itens 1 a 11).")

    respostas: List[int] = []
    for i in range(1, BSL_COMP_N_ITEMS + 1):
        val = _input_int_range(f"Item C{i:02d} (0-4): ", BSL_COMP_MIN, BSL_COMP_MAX)
        respostas.append(val)

    soma = sum(respostas)
    media = soma / BSL_COMP_N_ITEMS

    return BSLComplementarResult(
        respostas=respostas,
        soma=soma,
        media=media,
    )


def imprimir_relatorio_bsl23(res: BSL23Result) -> None:
    print("\n========== RESULTADO BSL-23 ==========")
    print(f"Itens respondidos: {len(res.respostas)}/23")
    print(f"Soma total: {res.soma} (mín=0 | máx=92)")
    print(f"Média de severidade: {res.media:.2f} (escala 0–4)")
    print(f"Classificação: {res.classificacao}")
    if res.qualidade_vida_percent is not None:
        print(f"Qualidade de vida (autoavaliação): {res.qualidade_vida_percent}%")
    print("======================================")


def imprimir_relatorio_complementar(res: BSLComplementarResult) -> None:
    print("\n====== RESULTADO BSL COMPLEMENTAR ======")
    print(f"Itens respondidos: {len(res.respostas)}/11")
    print(f"Soma total: {res.soma} (mín=0 | máx=44)")
    print(f"Média de frequência: {res.media:.2f} (escala 0–4)")
    print("========================================")


def main():
    print("======================================")
    print("  Sistema de Correção – BSL-23 (BR)   ")
    print("======================================")

    res_bsl23 = aplicar_bsl23()
    imprimir_relatorio_bsl23(res_bsl23)

    if _input_yes_no("\nDeseja aplicar também o BSL Complementar? (s/n): "):
        res_comp = aplicar_bsl_complementar()
        imprimir_relatorio_complementar(res_comp)

    print("\nFinalizado.")


if __name__ == "__main__":
    main()
