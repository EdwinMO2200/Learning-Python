def run():

    capital_pais = {
        'Francia' : "Paris",
        'España' : "Madrid",
        'Inglaterra' : "Londres",
        'Italia': "Roma",
    }

    for pais, capital in capital_pais.items():
        print('la capital de ' + pais + ' es ' + str(capital))

if __name__ == '__main__':
    run()