import re
import pandas as pd
from pathlib import Path
from paths import TABELAS_NCP
from datetime import date

# =========================
# UTILIDADES DE IDADE
# =========================

def idade_em_meses(anos: int, meses: int) -> int:
    if anos < 0 or meses < 0 or meses > 11:
        raise ValueError("Idade inválida")
    return anos * 12 + meses



def idade_anos_meses(nascimento: date, avaliacao: date) -> tuple[int, int]:
    if avaliacao < nascimento:
        raise ValueError("Data de avaliação não pode ser anterior ao nascimento")

    anos = avaliacao.year - nascimento.year
    meses = avaliacao.month - nascimento.month

    if avaliacao.day < nascimento.day:
        meses -= 1

    if meses < 0:
        anos -= 1
        meses += 12

    return anos, meses


# =========================
# LEITURA DAS FAIXAS
# =========================

def carregar_faixas_ncp() -> list[dict]:
    faixas = []

    for arquivo in TABELAS_NCP.glob("idade_*.csv"):
        nome = arquivo.stem

        match = re.match(r"idade_(\d+)-(\d+)-(\d+)-(\d+)$", nome)
        if not match:
            match = re.match(r"idade_(\d+)-(\d+)_(\d+)-(\d+)$", nome)
            if not match:
                continue

        a1, m1, a2, m2 = map(int, match.groups())

        min_meses = idade_em_meses(a1, m1)
        max_exclusivo = idade_em_meses(a2, m2) + 1  # torna faixa não ambígua

        faixas.append({
            "min": min_meses,
            "max_exclusivo": max_exclusivo,
            "arquivo": arquivo
        })

    if not faixas:
        raise RuntimeError("Nenhuma tabela NCP válida encontrada")

    faixas.sort(key=lambda f: f["min"])
    return faixas

# =========================
# SELEÇÃO DA TABELA
# =========================

from pathlib import Path

def obter_arquivo_ncp(anos: int, meses: int) -> Path:
    idade_meses = idade_em_meses(anos, meses)
    faixas = carregar_faixas_ncp()

    for faixa in faixas:
        if faixa["min"] <= idade_meses < faixa["max_exclusivo"]:
            return faixa["arquivo"]  # Path

    raise ValueError(f"Idade fora das faixas etárias NCP: {anos}a {meses}m")



