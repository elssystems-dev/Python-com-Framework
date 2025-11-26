from classes.TiposPessoa import Contribuinte, Fisico, Juridico

def main():
    while True:
        try:
            quantidadeColaboradores = int(input("Digite a quantidade de contribuintes: "))
            if quantidadeColaboradores < 0:
                raise ValueError
            break
        except ValueError:
            print("Escreva um número maior que zero.")

    colaboradores = []

    print("PARA PESSOA FÍSICA:\n[NOME], [RENDA ATUAL], [GASTO EM R$ COM SAÚDE]")
    print("PARA PESSOA JURÍDICA:\n[NOME], [RENDA ATUAL], [NÚMERO DE FUNCIONÁRIOS]\n\n")


    for i in range(quantidadeColaboradores):
        nome = input("Digite o [NOME]: ")
        renda = float(input("Digite a [RENDA ATUAL] em R$: "))

        opcao = input("\nTipo contribuinte:\n1- Pessoa Física\n2- Pessoa Jurídica\nResposta: ")
        if opcao == "1":
            gastoSaude = float(input("Digite o [GASTO COM SAÚDE] em R$: "))
            colaborador = Fisico(nome, renda, gastoSaude)
        else:
            numeroFuncionarios = int(input("Digite o [NÚMERO DE FUNCIONÁRIOS]: "))
            colaborador = Juridico(nome, renda, numeroFuncionarios)

        colaboradores.append(colaborador)

    for j in range(quantidadeColaboradores):
        print(colaboradores[j])



if __name__ == "__main__":
    main()

