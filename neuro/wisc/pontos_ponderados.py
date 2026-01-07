import pandas as pd
from paths import TABELAS_A8, TABELAS_CD, TABELAS_NCP
from loader_ncp import obter_arquivo_ncp, idade_anos_meses

arquivo = obter_arquivo_ncp(10, 5)
df = pd.read_csv(TABELAS_NCP / str(arquivo))
print(arquivo.name)
def valor_no_intervalo(valor, celula):
    if pd.isna(celula) or celula == "-" or celula == "":
        return False

    if isinstance(celula, (int, float)):
        return valor == int(celula)

    if isinstance(celula, str):
        if "-" in celula:
            inicio, fim = celula.split("-")
            return int(inicio) <= valor <= int(fim)
        else:
            return valor == int(celula)

    return False


def buscar_pp(df, coluna, valor_bruto):
    for _, linha in df.iterrows():
        if valor_no_intervalo(valor_bruto, linha[coluna]):
            return linha["PP"]
    raise ValueError(f"Valor {valor_bruto} não encontrado na coluna {coluna}")


resultados_pp = {}

subtestes = ['CB', 'SM', 'DG', 'CN', 'CD', 'VC', 'SNL', 'RM', 'CO', 'PS']
for subteste in subtestes:
    while True:
        try:
            valor_bruto = int(input(f"Digite o valor bruto do subteste {subteste}: "))
            pp = buscar_pp(df, subteste, valor_bruto)
            resultados_pp[subteste] = pp
            break
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")

print("\nResultados (PP):")
for subteste, pp in resultados_pp.items():
    print(f"{subteste}: PP = {pp}")
