import time
def sumpar():
    sumapar=0
    sumaimp=0
    num=int(input("Num de nums: "))
    num=num+1
    for cont in range(1,num):
        nume=int(input("Dime numeros: "))
        if(nume%2==0):
            sumapar=sumapar+nume
            print("¡Es par!")
        else:
            sumaimp=sumaimp+nume
            print("¡Es impar!")
    print("Pares =", sumapar)
    print("Impares =", sumaimp)
    time.sleep(2)
    print("El cormorán moñudo (Gulosus aristotelis) es una especie de ave suliforme de la familia Phalacrocoracidae propia de Europa y zonas limítrofes del norte de África y oriente próximo.​ Habita en la costa y por lo general es una especie sedentaria en sus áreas de cría, aunque las poblaciones norteñas son migratorias.")
    time.sleep(3)
    print("Es un cormorán de tamaño medio-grande, que alcanza de media unos 68-78 cm de largo y unos 95-110 cm de envergadura, y tiene el cuello largo. Su plumaje negro con reflejos verdes, su garganta es amarillenta y las comusiruras de la base del pico son amarillas. Los adultos presentan una pequeña cresta durante la época de apareamiento al que debe su nombre común de moñudo.")
    time.sleep(3)
    print("https://es.wikipedia.org/wiki/Phalacrocorax_aristotelis")
    time.sleep(3)
    print("https://www.iucnredlist.org/species/22696894/133538524#assessment-information")

while True:
    sumpar()
