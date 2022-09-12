
def run():
    divisibles_cinco = []
    divisibles_nueve = []
    for num in range(500,700,+1):
        if num % 5 == 0:
            divisibles_cinco.append(num)
        elif num % 9 == 0:
            divisibles_nueve.append(num)
    else:
        divisibles_nueve.append(num)

    print("Los numeros divisibles entre 9 son")
    print(divisibles_nueve) 

    print("Los numeros divisibles entre 5 son")
    print(divisibles_cinco)
if __name__ == '__main__':
    run()