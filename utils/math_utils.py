# def calcula_idade(ano_atual, ano_nascimento):
#     """
#     Calcula a idade de acordo com o ano atual e o ano de nascimento.
#     :param ano_atual: O ano atual
#     :param ano_nascimento: O ano de nascimento
#     :return: idade conforme o ano de nascimento
#     """
#     idade = ano_atual - ano_nascimento
#     return idade


def converter_temperatura(celsius):
    """
    :param celsius: Temperatura em Celsius
    :return: Conversão da temperatura em Fahreinheit e em Kelvin
    """
    fahrenheit = celsius * 1.8 + 32
    kelvin = celsius + 273
    return fahrenheit, kelvin


def informar_temperatura():
    """
    :return: Temperatura em Celsius
    """
    celsius = float(input('Informe a temperatura em celsius: '))
    return celsius


def soma(numero, numero2):
    """
    :param numero: Digite o número desejado
    :param numero2: Digite o número desejado
    :return: A soma dos dois números
    """
    return numero + numero2


def subtracao(numero, numero2):
    """
    :param numero: Digite o número desejado
    :param numero2: Digite o número desejado
    :return: A subtração dos dois números
    """
    return numero - numero2


def multiplicacao(numero, numero2):
    """
    :param numero: Digite o número desejado
    :param numero2: Digite o número desejado
    :return: A multiplicação dos dois números
    """
    return numero * numero2


def divisao(numero, numero2):
    """
    :param numero: Digite o número desejado
    :param numero2: Digite o número desejado
    :return: A divisão dos dois números
    """
    return numero / numero2


def solicitar_numero():
    """
    :return: Digite os números desejados para realizar a operação
    """
    numero1 = int(input("digite o numero que deseja para realizar a operação: "))
    numero2 = int(input("digite o numero que deseja para realizar a operação: "))
    return numero1, numero2

def calculadora():
    """
    :return: Escolha da operação desejada
    """
    print("[1] Adição")
    print("[2] Subtração")
    print("[3] Multiplicação")
    print("[4] divisão")
    print("[0] Sair")
    while True:

        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            numero1, numero2 = solicitar_numero()
            resultado = soma(numero1, numero2)
            print(f"a soma do {numero1} mais o {numero2} é igual a {resultado}")

        elif escolha == '2':
            numero1, numero2 = solicitar_numero()
            resultado = subtracao(numero1, numero2)
            print(f"a subtração do {numero1} menos o {numero2} é igual a {resultado}")


        elif escolha == '3':
            numero1, numero2 = solicitar_numero()
            resultado = multiplicacao(numero1, numero2)
            print(f"A multiplicação do {numero1} vezes o {numero2}é igual a  {resultado}")



        elif escolha == '4':
            numero1, numero2 = solicitar_numero()
            resultado = divisao(numero1, numero2)
            i = 1
            while i <= 10:
                print(f"{numero1} dividido pelo {numero2} é igual a {resultado}")
                i /= 1
                break

        elif escolha == '0':
            print("Saindo do programa.")
            break


def solicitapeso():
    while True:
        try:
            solicitapeso = float(input("Digite em KG (quilos), o seu peso: "))
            altura = float(input("Digite sua altura em metros: "))
            imc = solicitapeso / (altura ** 2)
            print("O IMC é de:", imc)

            if imc < 18.5:
                print("Você está abaixo do peso")
            elif 18.5 <= imc < 25:
                print("Você está com o peso adequado")
            elif 25 <= imc < 30:
                print("Você está em sobrepeso")
            else:
                print("Nível de obesidade")
            break
        except ValueError:
            print("Insira apenas números")
