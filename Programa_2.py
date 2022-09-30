# Segundo (y tercer) día de clase, calculador de media
def calcumadora():
    import statistics
    
    print("MEDIUM CALCULATUM")
    n1 = float(input("Numero1: "))
    n2 = float(input("Numero2: "))
    n3 = float(input("Numero3: "))
    print(statistics.median([n1, n2, n3]))
    if statistics.median([n1, n2, n3]) < 5:
        print("Suspendido")
        nombre = input("¿Como te llamas? ")
        if nombre == "Carlos":
            print("entonces aprobado :)")
        else:
            print("pues te quedas con tu" , statistics.median([n1, n2, n3] ))
    else:
        print("Aprobado")
    gon = input ()
    if gon == ("GONZALO TOBAJAS"):
        print("Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtag")
calcumadora()
