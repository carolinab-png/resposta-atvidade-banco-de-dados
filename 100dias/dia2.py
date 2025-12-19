print("Bem vindo a calculadora de gorjeta!")
conta= float(input("qual o valor da conta?"))
taxa= int(input("qual o valor da taxa? 8, 10 ou 12%"))
clientes= int(input("quantas pessoas vão dividir a conta?"))
total = taxa / 100 *conta + conta
valor_individual = total / clientes
print("cada pessoa vai pagar", valor_individual)