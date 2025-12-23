from loader_ncp import carregar_tabela_ncp

def main():
    print("=== Seleção automática da tabela NCP ===")

    anos = int(input("Digite a idade em anos: "))
    meses = int(input("Digite a idade em meses (0–11): "))

    df = carregar_tabela_ncp(anos, meses)

    print("\nTabela carregada com sucesso:")
    print(df.head())


if __name__ == "__main__":
    main()
