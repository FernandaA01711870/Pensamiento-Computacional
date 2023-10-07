#Importar la libreria math
import math

#Imprimimos un mensaje de bienvenida opara el usuario
print("Bienvenido a su calculadora de áreas y perímetros\n")

print("Indique si quiere calcular perimetros o áreas: \n")

#Creamos una lista que contenga las opciones del menú
opciones_principales = ["Perimetros","Areas","Salir",]

#Declarar las funciones de perimetro que vamos a utilizar
def perimetro_cuadrado (a):
  return a*4

def perimetro_triangulo (a,b,c): 
  return a + b + c

def perimetro_rectangulo (a, b):
  return 2 * (b + a)

def perimetro_paralelogramo (a, b):
  return 2 * (b +a)

def perimetro_rombo (a):
  return a*4

def perimetro_trapecio (B, b, a, c):
  return B + b + a + c

def perimetro_circulo (r):
  return 2 * math.pi * r

def perimetro_poligono (n,b):
  return n*b

#Declarar las funciones de áreas que vamos a utilizar
def area_cuadrado (a):
   return a**2

def area_triangulo (b, h): 
  return (b * h) / 2

def area_rectangulo (b, a):
  return  b * a

def area_paralelogramo (b, h):
  return b * h

def area_rombo (D, d):
  return (D*d)/2

def area_trapecio (B, d, h):
  return ((B + d)*h)/2

def area_circulo (r):
  return math.pi * r**2

def area_poligono (n, b, a):
  return (n*b)*a/2

def menu_principal():
    while True:
        print("Hola :D")

#Una funcion main que nos permitira regresar o salir del menu y del programa en si
def volver_main():
  opcion=input("¿Desea regresar al menú principal o desea salir de la app?\n\nDigite regresar o salir\n\n").lower()
  if opcion=="regresar":
    main()
  elif opcion == "salir":
    print("\nHasta luego :D")
  else:
    print("Digite una opcion correcta")

#Menú de perimetros
def menu_perimetros():
    
  menu_perimetro = 0

  while True:
      
    print("Bienvenido al menú de perimetros\n")
    print("Indique de que figura le gustaria conocer su perimetro\n")
      
    menu_perimetro = int(input("1- Cuadrado\n2- Triangulo\n3- Rectangulo\n4- Paralelogramo\n5- Rombo \n6- Trapecio\n7- Circulo\n8- Poligono Regular\n9- Regresar al menú principal\n"))
      
    if menu_perimetro == 1:
      num1 = float(input("Ingrese un lado del cuadrado: "))
      
      print("El perimetro del cuadrado es: ", perimetro_cuadrado(num1), "\n")
      break
        
    elif menu_perimetro == 2:
      num1 = float(input("Ingrese un lado del triangulo: "))
      num2 = float(input("Ingrese el segundo lado del triangulo: "))
      num3 = float(input("Ingrese el tercer lado del triangulo :"))

      print("El perimetro del trinagulo es: ", perimetro_triangulo(num1,num2,num3), "\n")
      break
      
    elif menu_perimetro == 3:
      num1 = float(input("Ingrese la altura del rectangulo: "))
      num2 = float(input("Ingrese la base del rectangulo: "))

      print("El perimetro del rectangulo es: ", perimetro_rectangulo(num1,num2), "\n")
      break
        
    elif menu_perimetro == 4:
      num1 = float(input("Ingrese la altura del paralelogramo: "))
      num2 = float(input("Ingrese la base del paralelogramo: "))

      print("El perimetro del paralelogramo es: ", perimetro_paralelogramo(num1,num2), "\n")
      break
        
    elif menu_perimetro == 5:
      num1 = float(input("Ingrese un lado del rombo: "))

      print("El perimetro del rombo es: ", perimetro_rombo(num1), "\n")
      break
        
    elif menu_perimetro == 6:
      num1 = float(input("Ingrese la base mayor del trapecio: "))
      num2 = float(input("Ingrese la base menor del trapecio: "))
      num3 = float(input("Ingrese un lado del trapecio: "))
      num4 = float(input("Ingrese el segundo lado del trapecio: "))

      print("El perimetro del trapecio es: ", perimetro_trapecio(num1,num2,num3,num4), "\n")
      break
      
    elif menu_perimetro == 7:
      num1 = float(input("Ingrese el radio del circulo: "))

      print("El perimetro del circulo es: ", perimetro_circulo(num1), "\n")
      break
        
    elif menu_perimetro == 8:
      num1 = float(input("Ingrese el numero de lados del poligono: "))
      num2 = float(input("Ingrese un lado del poligono: "))

      print("El perimetro del poligono es: ", perimetro_poligono(num1,num2), "\n")
      break

    elif menu_perimetro == 9:
      break
      main()
      
    else:
        print("Por favor digite una opción correcta")
  volver_main()
        
#Menú de areas
  
def menu_areas():

  menu_area = 0

  while True:
      
    print("Bienvenido al menú de áreas\n")
    print("Indique de que figura le gustaria conocer su área\n")
      
    menu_area = int(input("1- Cuadrado\n2- Triangulo\n3- Rectangulo\n4- Paralelogramo\n5- Rombo \n6- Trapecio\n7- Circulo\n8- Poligono Regular \n9- Regresar al menú principal \n\n"))
      
    if menu_area == 1:
      num1 = float(input("Ingrese un lado del cuadrado: "))

      print("El área del cuadrado es: " , area_cuadrado(num1), "\n")
      break
        
    elif menu_area == 2:
      num1 = float(input("Ingrese la base del triangulo: "))
      num2 = float(input("Ingrese la altura del triangulo :"))

      print("El área del triangulo es: ", area_triangulo(num1,num2), "\n")
      break
      
    elif menu_area == 3:
      num1 = float(input("Ingrese la altura del rectangulo: "))
      num2 = float(input("Ingrese la base del rectangulo: "))
        
      print("El area del rectangulo es: ", area_rectangulo(num1,num2), "\n")
      break
        
    elif menu_area == 4:
      num1 = float(input("Ingrese la altura (h) del paralelogramo: "))
      num2 = float(input("Ingrese la base del paralelogramo: "))

      print("El área del paralelogramo es: ", area_paralelogramo(num1,num2), "\n")
      break
        
    elif menu_area == 5:
      num1 = float(input("Ingrese la diagonal mayor del rombo: "))
      num2 = float(input("Ingrese la diagonal menor del rombo: "))
        
      print("El area del rombo es: ", area_rombo(num1,num2), "\n")
      break
        
    elif menu_area == 6:
      num1 = float(input("Ingrese la base mayor del trapecio: "))
      num2 = float(input("Ingrese la base menor del trapecio: "))
      num3 = float(input("Ingrese la altura (h) del trapecio: "))
        
      print("El area del trapecio es: ", area_trapecio(num1,num2,num3), "\n")
      break
    
    elif menu_area == 7:
      num1 = float(input("Ingrese el radio del circulo: "))

      print("El area del circulo es: ", area_circulo(num1), "\n")
      break
        
    elif menu_area == 8:
      num1 = float(input("Ingrese el numero de lados del poligono: "))
      num2 = float(input("Ingrese un lado del poligono: "))
      num3 = float(input("Ingrese la apotema: "))
        
      print("El area del poligono es: ", area_poligono(num1,num2,num3), "\n")
      break
      
    elif menu_area == 9:
      break
    
    else:
      print("\n\nPor favor digite una opción correcta")
  volver_main()

#Funcion main con el menú principal

def main():
  for i, opcion in enumerate(opciones_principales, start=1):
      print(f"{i}. {opcion}")
  
  menu_principal = int(input("Elija una opcion: "))
  
  if menu_principal == 1:
    menu_perimetros()
  elif menu_principal == 2:
    menu_areas()
  elif menu_principal == 3:
    print("\n\nAdios, regrese pronto :D\n")
#Si ninguna opción se cumple mostar un mensaje de error
  else:
    print("Por favor digite una opción correcta \n")  

  
main()
