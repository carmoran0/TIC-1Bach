# BANCO
def banco():
    bal=0
    print("Los costes de operacion son de un 0,01%")
    while True:
        print("Tienes ",bal, "$")
        num=input("¿Quieres retirar o ingresar? [I/R] ")
        if num=="I":
            val=int(input("¿Cantidad? "))
            if val<0:
                print("No puedes números negativos")
            else:
                val = val - val*0.01
                print("Costes de operacion: ",val*0.01, "$")
                bal = bal + val
        if num=="R":
            val=int(input("¿Cantidad? "))
            if val>bal:
                print("NO PUEDES RETIRAR MAS DE LO QUE TIENES")
            else:
                val = val + val*0.01
                print("Costes de operacion: ",val*0.01, "$")
                bal = bal - val
while True:
    banco()
