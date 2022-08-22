'''
Cálculo de IRPF em Phyton
Aula 04 - Nivelamento em Programação
Por Douglas Campos
05/08/2022
'''
informeCorretoPensao = 'n'
informeCorretoDeducao = 'n'
informeCorretoRendimento = 'n'
informeCorretoDependentes = 'n'
valorPensaoCalculo = 0
valorDeducaoCalculo = 0
valorRedimentoMensal = 0
valorDependentes = 0
imposto = 0
userFaixa = 0

print("=" * 70)
print(" " * 8, end="")
print("\033[1m\033[94m+-+- BEM VINDO AO SEU SISTEMA DE CÁLCULO DE IRPF -+-+\033[0m")
print("=" * 70)

nomeUsuario = input("\nPor favor informe seu nome: ")

redimentoMensal = input("\nPor favor, informe seu salário bruto mensal: ")
while informeCorretoRendimento != 's':
    try:
        float(redimentoMensal)
        informeCorretoRendimento = 's'
        valorRedimentoMensal= float(redimentoMensal)
    except ValueError:
        print("\033[91m\nPor favor informe corretamente sobre seu salário bruto em formato de números.\033[0m")
        redimentoMensal = input("Por favor, informe seu salário bruto mensal: ")
        informeCorretoRendimento = 'n'

numeroDependentes = input("\nPor favor, informe o número de dependentes que possui: ")
while informeCorretoDependentes != 's':
    try:
        int(numeroDependentes)
        informeCorretoDependentes = 's'
        valorDependentes = int(numeroDependentes)
    except ValueError:
        print("\033[91m\nPor favor informe corretamente sobre seu salário bruto em formato de números.\033[0m")
        numeroDependentes = input("Por favor, informe o número correto de dependentes que possui: ")
        informeCorretoDependentes = 'n'

sePagaPensao = input("\nVocê efetua pagamento de pensão alimentícia? (s/n): ")
while informeCorretoPensao != 's':
    if sePagaPensao.lower() == 's':
        valorPensao = input("Por favor, nos informe o valor da pensão alimentícia: ")
        try:
            float(valorPensao)
            informeCorretoPensao = 's'
            valorPensaoCalculo = float(valorPensao)
        except ValueError:
            print("\n\033[91mPor favor informe corretamente sobre deduções em formato de números inteiro.\033[0m")
            informeCorretoPensao = 'n'
    elif sePagaPensao.lower() == 'n':
        valorPensao = 0
        informeCorretoPensao = 's'
    else:
        print("\033[91mPor favor informe corretamente sobre pensão alimentícia.\033[0m")
        sePagaPensao = input("Você efetua pagamento de pensão alimentícia? (s/n): ")

sePagaDeducoes = input("\nExiste alguma dedução em seu ordenado? (s/n): ")
while informeCorretoDeducao != 's':
    if sePagaDeducoes.lower() == 's':
        valorDeducao = input("Por favor, nos informe o valor da dedução: ")
        try:
            float(valorDeducao)
            informeCorretoDeducao = 's'
            valorDeducaoCalculo = float(valorDeducao)
        except ValueError:
            print("\033[91m\nPor favor informe corretamente sobre deduções em formato de números inteiro.\033[0m")
            informeCorretoDeducao = 'n'
    elif sePagaDeducoes.lower() == 'n':
        valorDeducao = 0
        informeCorretoDeducao = 's'
    else:
        print("\n\033[91mPor favor informe corretamente sobre deduções.\033[0m")
        sePagaDeducoes = input("Existe alguma dedução em seu ordenado? (s/n): ")

baseCalculo = valorRedimentoMensal - (valorDependentes * 189.59) - valorPensaoCalculo - valorDeducaoCalculo

if baseCalculo > 4664.68:
    imposto = imposto + ((baseCalculo - 4664.68) * 0.275)
    baseCalculo = 4664.68
    userFaixa = 5
if baseCalculo > 3751.05:
    imposto = imposto + ((baseCalculo - 3751.05) * 0.225)
    baseCalculo = 3751.05
    if userFaixa == 0:
        userFaixa = 4
if baseCalculo > 2826.65:
    imposto = imposto + ((baseCalculo - 2826.65) * 0.15)
    baseCalculo = 2826.65
    if userFaixa == 0:
        userFaixa = 3
if baseCalculo > 1903.98:
    imposto = imposto + ((baseCalculo - 1903.98) * 0.075)
    baseCalculo = 1903.98
    if userFaixa == 0:
        userFaixa = 2
else:
    if userFaixa == 0:
        userFaixa = 1

taxaEfetiva = round((imposto / baseCalculo) * 100, 2)

print("\n")
print("=" * 70)
print(" " * 15, end="")
print("\033[1m\033[94m+-+- RESULTADO DO CÁLCULO DE IRPF -+-+\033[0m")
print("=" * 70)
if userFaixa == 1:
    print("\nSr(a).\033[94m", nomeUsuario, "\033[0m")
    print("O Sr(a). se encontra na \033[91mfaixa", userFaixa, "\033[0mde recolhimento de IR")
    print("\033[94mSendo assim está insento de pagamento de imposto\033[0m\n")
else:
    print("\nSr(a).\033[94m", nomeUsuario, "\033[0mabaixo os valores calculados")
    print("O valor do imposto devido é de \033[91mR$", round(imposto, 2), "\033[0m")
    print("O Sr(a). se encontra na \033[91mfaixa",userFaixa, "\033[0mde recolhimento de IR")
    print("A taxa efetiva aplicada é de \033[91mR$ ", taxaEfetiva, "%\033[0m\n", sep="")
print("=" * 70)