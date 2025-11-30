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

    print("\n===== RESULTADOS =====\n")
    for pessoa in colaboradores:
        print(f"Contribuinte: {pessoa._nome}")
        print(f"Renda Atual: R${pessoa._rendaAtual:.2f}")
        # Tenta usar gastosSaude: se existir, é PF
        try:
            print(f"Gastos com Saúde: R${pessoa._gastosSaude:.2f}")
            print(pessoa.definicaoImposto(pessoa._rendaAtual, pessoa._gastosSaude))
        except:
            # Se não tiver gastosSaude, é PJ
            print(f"Número de Funcionários: {pessoa._numeroFuncionarios}")
            print(pessoa.definicaoImposto(pessoa._rendaAtual, pessoa._numeroFuncionarios))


if __name__ == "__main__":
    main()

