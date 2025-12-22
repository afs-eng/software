from paths import TABELAS_A8, TABELAS_CD, TABELAS_NCP
import pandas as pd

# arquivo excel
#df = pd.read_excel(TABELAS_A8 / "Tabela_A8_4_idades_10_0a10_11.xlsx", engine="openpyxl")

# arquivo csv
df = pd.read_csv(TABELAS_NCP / 'tabela_a1.csv')

print(df.head())

