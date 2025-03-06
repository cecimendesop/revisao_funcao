from utils.math_utils import *

# ano_atual = int(input('Digite o ano atual: '))
# ano_nascimento = int(input('Digite seu ano de nascimento: '))

# print("Você tem",(ano_atual, ano_nascimento), "anos")


fahrenheit, kelvin = converter_temperatura(informar_temperatura())
print("Temperatura em Fahreinheit: ", fahrenheit)
print("Temperatura em Kelvin: ", kelvin)

calculadora()

solicitapeso()