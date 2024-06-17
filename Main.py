
def mostrar_menu():
    print("Bienvenido al menu")
    print("Elige el set de datos a ser utilizado:")
    print("\t 1. Set de peliculas 1")
    print("\t 2. Set de peliculas 2")
    setdatos = input("Selecciona una opcion: ")

    print("Elige el set de datos a ser utilizado:")
    print("\t 1. Sistema de recomendación simple")
    print("\t 2. Sistema de recomendación colaborativo")
    sistema = input("Selecciona una opcion: ")

    return setdatos, sistema

def recomend(sistema,fitxer1, fitxer2):
    
    if sistema == "1":
        reco = Recomanacio_Simple()
    else :
        reco = Recomanacio_Colaborativa()

    reco.dades_pelicula(fitxer1)
    reco.dades_ratings(fitxer2)
    reco.calcula_mitjanes()

def main():
    datos, sistema= mostrar_menu()
    
    if datos == "1":
        fitxers = fitxer1, fitxer2
    elif datos == "2":
        fitxers = fitxer1, fitxer2
    else:
        #Error
        pass

    if sistema == "1":
        recomend(sistema,fitxer1, fitxer2)
    elif sistema == "2":
        pass
    else:
        # Error
        pass


if __name__ == "__main__":
    main()