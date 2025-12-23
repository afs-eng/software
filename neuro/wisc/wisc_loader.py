import pandas as pd
from pathlib import Path
import sys
from paths import TABELAS_NCP

def get_age_table_path(years, months):
    """
    Retorna o caminho do arquivo CSV correspondente à idade fornecida.
    Baseado no manual WISC-IV, tabelas A.1 a A.33.
    """
    total_months = years * 12 + months
    
    # Validação básica de faixa etária do WISC-IV (6:0 a 16:11)
    # 6 anos = 72 meses
    # 16 anos e 11 meses = 203 meses
    if total_months < 72 or total_months > 203:
        return None

    # O WISC-IV divide as tabelas em intervalos de 4 meses
    # Começando em 6:0 (72 meses)
    # Intervalo 0: 72-75 (6:0 - 6:3)
    # Intervalo 1: 76-79 (6:4 - 6:7)
    # ...
    
    # Calcular o início do intervalo de 4 meses
    months_from_start = total_months - 72
    interval_index = months_from_start // 4
    
    start_total_months = 72 + (interval_index * 4)
    end_total_months = start_total_months + 3
    
    # Converter de volta para anos e meses
    start_year = start_total_months // 12
    start_month = start_total_months % 12
    
    end_year = end_total_months // 12
    end_month = end_total_months % 12
    
    # Construir o nome do arquivo
    # Padrão identificado: idade_Y-M-Y-M.csv
    filename = f"idade_{start_year}-{start_month}-{end_year}-{end_month}.csv"
    
    return TABELAS_NCP / filename

def load_ncp_table(years, months):
    """
    Carrega a tabela NCP correta para a idade especificada.
    """
    file_path = get_age_table_path(years, months)
    
    if not file_path:
        raise ValueError(f"Idade fora do intervalo suportado (6:0 a 16:11): {years} anos e {months} meses")
        
    if not file_path.exists():
        raise FileNotFoundError(f"Arquivo de tabela não encontrado para {years}a {months}m: {file_path}")
        
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        raise RuntimeError(f"Erro ao ler arquivo CSV {file_path}: {e}")

def parse_interval_value(value_str):
    """
    Analisa uma string de intervalo (ex: '0-2', '16-18', '32:13') e retorna uma lista de inteiros.
    Trata erros comuns de OCR como ':' em vez de '-'.
    """
    if pd.isna(value_str):
        return []
        
    value_str = str(value_str).strip()
    if not value_str:
        return []
        
    # Se for apenas um número
    if value_str.isdigit():
        return [int(value_str)]
        
    # Substituir separadores incorretos
    value_str = value_str.replace(':', '-')
    
    if '-' in value_str:
        try:
            parts = value_str.split('-')
            if len(parts) == 2:
                start = int(parts[0])
                end = int(parts[1])
                return list(range(start, end + 1))
        except ValueError:
            pass
            
    return []

def get_ponderado(score_bruto, subteste, df_table):
    """
    Busca o ponto ponderado para um dado score bruto em um subteste específico.
    """
    # Normaliza nome do subteste
    subteste = subteste.upper().strip()
    
    # Mapeamento de nomes de colunas (pode variar nos CSVs)
    col_map = {
        'CUBOS': ['CB', 'C B'],
        'SEMELHANCAS': ['SM', 'SM_', 'S M'],
        'DIGITOS': ['DG', 'D G'],
        'CONCEITOS': ['CN', 'C N', 'CNF'],
        'CODIGOS': ['CD', 'C D'],
        'VOCABULARIO': ['VC', 'V C'],
        'SEQUENCIA': ['SNL', 'SNI', 'S N L'],
        'MATRICIAL': ['RM', 'R M'],
        'COMPREENSAO': ['CO', 'C O'],
        'PROCURAR': ['PS', 'P S']
    }
    
    target_col = None
    for possible_name in col_map.get(subteste, [subteste]):
        if possible_name in df_table.columns:
            target_col = possible_name
            break
            
    if not target_col:
        # Tenta encontrar coluna que contém o nome
        for col in df_table.columns:
            if subteste in col.upper():
                target_col = col
                break
    
    if not target_col:
        raise ValueError(f"Subteste '{subteste}' não encontrado na tabela.")
        
    # Itera pelas linhas para encontrar o intervalo que contém o score bruto
    for index, row in df_table.iterrows():
        cell_value = row[target_col]
        valid_scores = parse_interval_value(cell_value)
        
        if score_bruto in valid_scores:
            ponderado_col = df_table.columns[0] 
            return row[ponderado_col]
            
    return None

if __name__ == "__main__":
    print("Carregador de Tabelas NCP do WISC-IV")
    print("-------------------------------------")
    
    if len(sys.argv) == 3:
        # Modo script: python wisc_loader.py <anos> <meses>
        try:
            anos = int(sys.argv[1])
            meses = int(sys.argv[2])
            interactive = False
        except ValueError:
            print("Erro: Idade deve ser número inteiro.")
            sys.exit(1)
    else:
        # Modo interativo
        interactive = True
        try:
            anos_input = input("Digite a idade em anos (ex: 6): ")
            if not anos_input:
                sys.exit(0)
            anos = int(anos_input)
            
            meses_input = input("Digite a idade em meses (ex: 4): ")
            if not meses_input:
                meses = 0
            else:
                meses = int(meses_input)
        except ValueError:
            print("Erro: Por favor digite números inteiros válidos.")
            sys.exit(1)

    print(f"\nBuscando tabela para idade: {anos} anos e {meses} meses...")
    
    try:
        path = get_age_table_path(anos, meses)
        if path:
            print(f"Arquivo encontrado: {path.name}")
            print(f"Caminho completo: {path}")
            
            df = load_ncp_table(anos, meses)
            print(f"Tabela carregada com sucesso! ({len(df)} linhas)")
            print("\nPrimeiras 5 linhas da tabela:")
            print(df.head())
            
            # Opcional: Mostrar colunas disponíveis para ajudar o usuário
            print("\nSubtestes disponíveis (colunas):")
            print(", ".join(df.columns.tolist()))
            
        else:
            print("Não foi possível determinar o arquivo para essa idade.")
            print("Verifique se a idade está dentro da faixa do WISC-IV (6:0 a 16:11).")
            
    except Exception as e:
        print(f"ERRO: {e}")
