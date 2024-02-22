print("Hello, World!")
def simulador_aposentadoria(idade_atual, idade_aposentadoria, renda_anual, taxa_poupanca, taxa_retorno_investimento):
    saldo_acumulado = 0
    anos_para_aposentar = idade_aposentadoria - idade_atual

    for ano in range(anos_para_aposentar):
        saldo_acumulado += renda_anual * taxa_poupanca
        saldo_acumulado *= (1 + taxa_retorno_investimento)

    return saldo_acumulado

def main():
    print("Bem-vindo ao Simulador de Aposentadoria!")

    idade_atual = int(input("Informe sua idade atual: "))
    idade_aposentadoria = int(input("Informe a idade em que pretende se aposentar: "))
    renda_anual = float(input("Informe sua renda anual: "))
    taxa_poupanca = float(input("Informe a taxa de poupança (em decimal): "))
    taxa_retorno_investimento = float(input("Informe a taxa de retorno de investimento (em decimal): "))

    saldo_acumulado = simulador_aposentadoria(idade_atual, idade_aposentadoria, renda_anual, taxa_poupanca, taxa_retorno_investimento)

    print(f"\nSeu saldo acumulado ao se aposentar aos {idade_aposentadoria} anos será de: R$ {saldo_acumulado:.2f}")

if __name__ == "__main__":
    main()
