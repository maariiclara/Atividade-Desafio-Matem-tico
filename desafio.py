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
# COSSENO - IGOR

def cosseno(angulo):

    pi = 3.141592653589793

    # converter para radiano
    rad = angulo * pi / 180

    cos = 0
    k = 10

    for n in range(k):

        expoente = 2 * n

        # calcular fatorial
        fatorial = 1
        for i in range(1, expoente + 1):
            fatorial *= i

        termo = ((-1) ** n) * (rad ** expoente) / fatorial
        cos += termo

    return cos


# PARTE IGOR - COSSENO


# PARTE YASMIN - LOG NATURAL

print("----- Sistema de Log Natural -----")
print("")

x = float(input("Digite um número maior que 0: "))

while x <= 0:
    print("Número inválido!")
    x = float(input("Digite um número maior que 0: "))

arredondamento = int(input("Digite o máximo de repeticões que deseja (ideal, 20): "))

soma = 0
n = 0

while n <= arredondamento:
    termo = (1 / (2*n + 1)) * (((x - 1) / (x + 1)) ** (2*n + 1))
    soma = soma + termo
    n = n + 1

resultado = 2 * soma

print("")
print(f"ln({x}) ≈ {resultado}")


# PARTE PEDRO - EXPONENCIAL

def exponencial (x, termos=50):
    termo_atual = 1.0
    resultado = 1
    
    for i in range (1, termos):
        termo_atual = termo_atual * x / i
        resultado += termo_atual
        
    return resultado

x = float(input("digite seu numero: "))

print(exponencial(x))

# PARTE GUILHERME - PI

