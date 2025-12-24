from paths import TABELAS_A8, TABELAS_CD, TABELAS_NCP
import pandas as pd

# arquivo excel
#df = pd.read_excel(TABELAS_A8 / "Tabela_A8_4_idades_10_0a10_11.xlsx", engine="openpyxl")

# arquivo csv
df = pd.read_csv(TABELAS_NCP / 'idade_6-4-6-7.csv')



df.rename(columns={'Pontos Ponderado': 'PB'}, inplace=True )

df.to_csv('idade_6-4-6-7.csv', index=False)

print(df.head())