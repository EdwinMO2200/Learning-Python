def run():
    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print("Numeros del 1 al 20", numeros)
    def impares(lista):
        impares = []
        for n in lista:
            if n % 2 != 0:
                impares.append(n)
        return impares
    resultado = impares(numeros)
    print("Impares", resultado)
    print()
    def pares(lista):
        pares = []
        for n in lista:
            if n % 2 == 0:
                pares.append(n)
        return pares
    resultado = pares(numeros)
    print("Pares", resultado)
print()

if __name__ == '__main__':
    run()
