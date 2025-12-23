import re
import pandas as pd
from pathlib import Path
from paths import TABELAS_NCP


# =========================
# UTILIDADES DE IDADE
# =========================

def idade_em_meses(anos: int, meses: int) -> int:
    if anos < 0 or meses < 0 or meses > 11:
        raise ValueError("Idade inválida")
    return anos * 12 + meses


# =========================
# LEITURA DAS FAIXAS
# =========================

def carregar_faixas_ncp() -> list[dict]:
    faixas = []

    for arquivo in TABELAS_NCP.glob("idade_*.csv"):
        nome = arquivo.stem
        match = re.match(r"idade_(\d+)-(\d+)-(\d+)-(\d+)", nome)

        if not match:
            # Tentar formato alternativo com underscore (embora o glob mostre hífens)
            match = re.match(r"idade_(\d+)-(\d+)_(\d+)-(\d+)", nome)
            if not match:
                continue

        a1, m1, a2, m2 = map(int, match.groups())

        faixa = {
            "min": idade_em_meses(a1, m1),
            "max": idade_em_meses(a2, m2),
            "arquivo": arquivo
        }

        faixas.append(faixa)

    if not faixas:
        raise RuntimeError("Nenhuma tabela NCP válida encontrada")

    return faixas


# =========================
# SELEÇÃO DA TABELA
# =========================

def carregar_tabela_ncp(anos: int, meses: int) -> pd.DataFrame:
    idade_meses = idade_em_meses(anos, meses)
    faixas = carregar_faixas_ncp()

    for faixa in faixas:
        if faixa["min"] <= idade_meses <= faixa["max"]:
            return pd.read_csv(faixa["arquivo"], encoding="utf-8")

    raise ValueError("Idade fora das faixas etárias NCP")
