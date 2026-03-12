# PARTE MARIA - NÚMERO DE EULER
print("------- CALCULANDO O NÚMERO DE EULER -------")
def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado
termos = int(input("Digite o máximo de repetições que você deseja (o ideal seria 20): "))
def numero_e(termos):
    soma = 0
    for n in range(termos):
        soma = soma + 1 / fatorial(n)
    return soma
print(f"O Número de Euler tem o valor aproximado de: {numero_e(termos)}")
print("")

# PARTE GUSTAVO - SENO


# PARTE IGOR - COSSENO


# PARTE YASMIN - LOG NATURAL


# PARTE PEDRO - EXPONENCIAL


# PARTE GUILHERME - PI

