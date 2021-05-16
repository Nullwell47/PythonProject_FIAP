nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
if idade<65:
    prioridade="NÃO"
    print("O paciente " + nome + " possui atendimento prioritário? " + prioridade)
if idade>=65:
    prioridade="SIM"
    print("O paciente " + nome + " possui atendimento prioritário? " + prioridade)