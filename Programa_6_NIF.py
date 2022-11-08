def denei():
  numm=int(input("Introduzca el número del DNI:"))
  letritas='TRWAGMYFPDXBNJZSQVHLCKE'
  print('letra: ', letritas[numm%23])
 
while True:
  denei()
