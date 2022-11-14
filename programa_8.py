def esVocal(letra):
    respuesta=False
    if(letra=='a' or letra=='e' or letra=='i' or letra
         =='o' or letra=='u'):
         respuesta=True
    return(respuesta)

def deletreo():
    palabra-input("Dime una palabra: ")
    cuentavocales=0
    cuentaconsonantes=0
    for cont in range(0,len(palabra)):
        print(palabra[cont]+'')
        if(esVocal(palabra[cont])==True):
            cuentavocales=cuentavocales+1
        else:
            cuentaconsonantes=cuentaconsonantes+1
    print( "Tiene "+str(cuentavocales) +" vocales")
    print("Tiene "+str(cuentaconsonantes)-" consonantes"
    
deletreo()
