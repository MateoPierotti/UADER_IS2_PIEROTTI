import matplotlib.pyplot as plt

def collatz(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1
    return count

def calcular_collatz_para_rango(rango):
    resultados = []
    for num in range(1, rango + 1):
        resultado = collatz(num)
        resultados.append((num, resultado))
    return resultados

def graficar_collatz(resultados):
    numeros_iniciales = [resultado[0] for resultado in resultados]
    iteraciones = [resultado[1] for resultado in resultados]

    plt.figure(figsize=(10, 6))
    plt.scatter(iteraciones, numeros_iniciales, s=5, color='blue')
    plt.title('Número de Collatz: Iteraciones vs Número Inicial')
    plt.xlabel('Iteraciones')
    plt.ylabel('Número Inicial')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    resultados = calcular_collatz_para_rango(10000)
    graficar_collatz(resultados)
