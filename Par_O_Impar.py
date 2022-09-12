def run():
    num = int(input("Escoge un numero menor a 20: "))
    if num >0 & num < 9:
        print("Favorable")
    elif num > 10 & num <19:
        print("Moderada")
    elif num > 20 & num <29:
        print("Regular")
    elif num > 30 & num <49:
        print("Mala")
    elif num > 50:
        print("Peligrosa")
if __name__ == '__main__':
    run()
