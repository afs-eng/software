import pandas as pd
from pathlib import Path
import sys

# Adiciona o diretório pai ao path para importar paths.py se necessário
# Mas como estamos no mesmo diretório ou próximo, vamos tentar importar direto ou definir aqui.
# Para evitar problemas de importação, vou redefinir o caminho aqui baseando-se no arquivo atual.

BASE_DIR = Path(__file__).resolve().parent
TABELAS_NCP = BASE_DIR / "tabelas" / "tabelas-ncp"

