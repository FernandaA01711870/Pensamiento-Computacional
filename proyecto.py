#Importar la libreria math
import math


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

#Desplegar una serie de menús con distintas opciones a elejir

#Menú principal

menu_principal = 0

while True:

  print("Bienvenido a su calculadora de áreas y perímetros\n")

  print("Indique si quiere calcular perimetros o áreas:\n") 
  
  menu_principal = int(input("1- Perimetros\n2- Áreas\n3- Salir\n\n"))
  
#Menú de perimetros

  if menu_principal == 1: 
    
    menu_perimetro = 0

    while True:
      
      print("Bienvenido al menú de perimetros")
      print("Indique de que figura le gustaria conocer su perimetro\n")
      
      menu_perimetro = int(input("1- Cuadrado\n2- Triangulo\n3- Rectangulo\n4- Paralelogramo\n5- Rombo \n6- Trapecio\n7- Circulo\n8- Poligono Regular\n9- Regresar al menú principal\n"))

#Perimetro cuadrado
      if menu_perimetro == 1:
        num1 = float(input("Ingrese un lado del cuadrado: "))

#Comprobar que los valores sean validos
        if num1 <= 0:
         print("El valor ingresado es incorrecto")
        else: 
         print("\nEl perimetro del cuadrado es: ", perimetro_cuadrado(num1), "\n")

#Perimetro triangulo        
      elif menu_perimetro == 2:
        num1 = float(input("Ingrese un lado del triangulo: "))
        num2 = float(input("Ingrese el segundo lado del triangulo: "))
        num3 = float(input("Ingrese el tercer lado del triangulo :"))

#Comprobar que las longitudes del triangulo si pertenezcan a un triangulo
        if num1 + num2 > num3 and num1 + num3 > num2 and num2 + num3 > num1:
          print("\nEl perimetro del triangulo es: ", perimetro_triangulo(num1,num2,num3),"\n")
        else:
          print("\nLas longitudes no pertenecen a las de un triangulo\n")

#Perimetro rectangulo
      elif menu_perimetro == 3:
        num1 = float(input("Ingrese la altura del rectangulo: "))
        num2 = float(input("Ingrese la base del rectangulo: "))

#Comprobar que los valores sean validos        
        if num1 <= 0 or num2 <= 0:
          print("\nLos valores ingresados son incorrectos\n")
        else:
          print("\nEl perimetro del rectangulo es: ", perimetro_rectangulo(num1,num2),"\n")

#Perimetro paralelogramo        
      elif menu_perimetro == 4:
        num1 = float(input("Ingrese la altura del paralelogramo: "))
        num2 = float(input("Ingrese la base del paralelogramo: "))

#Comprobar que los valores sean validos        
        if num1 <= 0 or num2 <= 0:
          print("\nLos valores ingresados son incorrectos\n")
        else:
          print("\nEl perimetro del paralelogramo es: ", perimetro_paralelogramo(num1,num2),"\n")

#Perimetro rombo
      elif menu_perimetro == 5:
        num1 = float(input("Ingrese un lado del rombo: "))

#Comprobar que los valores sean validos        
        if num1 <= 0:
          print("\nLos valores ingresados son incorrectos\n")
        else:
          print("\nEl perimetro del rombo es: ", perimetro_rombo(num1),"\n")

#Perimetro trapecio       
      elif menu_perimetro == 6:
        num1 = float(input("Ingrese la base mayor del trapecio: "))
        num2 = float(input("Ingrese la base menor del trapecio: "))
        num3 = float(input("Ingrese un lado del trapecio: "))
        num4 = float(input("Ingrese el segundo lado del trapecio: "))

#Comprobar que los valores sean validos        
        if num1 <= 0 or num2 <= 0 or num3 <= 0 or num4 <= 0:
          print("\nLos valores ingresados son incorrectos\n")
        else: 
          print("\nEl perimetro del trapecio es: ", perimetro_trapecio(num1,num2,num3,num4),"\n")
 
 #Perimetro circulo     
      elif menu_perimetro == 7:
        num1 = float(input("Ingrese el radio del circulo: "))

#Comprobar que los valores sean validos        
        if num1 <= 0:
          print("\nLos valores ingresados son incorrectos\n")
        else:
          print("\nEl perimetro del circulo es: ", perimetro_circulo(num1),"\n")
 
 #Perimetro poligono       
      elif menu_perimetro == 8:
        num1 = float(input("Ingrese el numero de lados del poligono: "))
        num2 = float(input("Ingrese un lado del poligono: "))

#Comprobar que los valores sean validos        
        if num1 <= 0 or num2 <= 0:
          print("\nLos valores ingresados son incorrectos\n")
        else:
          print("\nEl perimetro del poligono es: ", perimetro_poligono(num1,num2), "\n")

      elif menu_perimetro == 9:
       break
        
      else:
        print("Por favor digite una opción correcta")
        
#Menú de areas
  
  elif menu_principal == 2:

    menu_area = 0

    while True:
      
     print("Bienvenido al menú de áreas\n")
     print("Indique de que figura le gustaria conocer su área\n")
      
     menu_area = int(input("1- Cuadrado\n2- Triangulo\n3- Rectangulo\n4- Paralelogramo\n5- Rombo \n6- Trapecio\n7- Circulo\n8- Poligono Regular \n9- Regresar al menú principal \n\n"))

#Área cuadrado      
     if menu_area == 1:
       num1 = float(input("Ingrese un lado del cuadrado: "))

#Comprobar que el valor sea valido
       if num1 <= 0:
        print("\nEl valor ingresado no es valido\n")
       else:
        print("\nEl área del cuadrado es: " , area_cuadrado(num1), "\n")
 
#Área triangulo        
     elif menu_area == 2:
        num1 = float(input("Ingrese la base del triangulo: "))
        num2 = float(input("Ingrese la altura del triangulo :"))

#Comprobar que el valor sea valido
        if num1 <= 0 or num2 <= 0:
          print("\nEl valor ingresado no es valido\n")
        else:
          print("\nEl área del triangulo es: ", area_triangulo(num1,num2), "\n")

#Área rectangulo      
     elif menu_area == 3:
        num1 = float(input("Ingrese la altura del rectangulo: "))
        num2 = float(input("Ingrese la base del rectangulo: "))

#Comprobar que el valor sea valido
        if num1 <= 0 or num2 <= 0:
          print("\nEl valor ingresado no es valido\n")
        else:
          print("\nEl area del rectangulo es: ", area_rectangulo(num1,num2), "\n")

 #Área paralelogramo       
     elif menu_area == 4:
        num1 = float(input("Ingrese la altura (h) del paralelogramo: "))
        num2 = float(input("Ingrese la base del paralelogramo: "))

#Comprobar que el valor sea valido
        if num1 <= 0 or num2 <= 0:
          print("\nEl valor ingresado no es valido\n")
        else:
          print("\nEl area del rectangulo es: ", area_rectangulo(num1,num2), "\n")

#Área rombo       
     elif menu_area == 5:
        num1 = float(input("Ingrese la diagonal mayor del rombo: "))
        num2 = float(input("Ingrese la diagonal menor del rombo: "))

#Comprobar que el valor sea valido
        if num1 <= 0 or num2 <= 0:
          print("\nEl valor ingresado no es valido\n")
        else:       
          print("\nEl area del rombo es: ", area_rombo(num1,num2), "\n")

#Área trapecio       
     elif menu_area == 6:
        num1 = float(input("Ingrese la base mayor del trapecio: "))
        num2 = float(input("Ingrese la base menor del trapecio: "))
        num3 = float(input("Ingrese la altura (h) del trapecio: "))

#Comprobar que el valor sea valido
        if num1 <= 0 or num2 <= 0 or num3 <= 0:
          print("\nEl valor ingresado no es valido\n")
        else:       
          print("\nEl area del trapecio es: ", area_trapecio(num1,num2,num3), "\n")

#Área circulo    
     elif menu_area == 7:
        num1 = float(input("Ingrese el radio del circulo: "))

#Comprobar que el valor sea valido
        if num1 <= 0:
          print("\nEl valor ingresado no es valido\n")
        else:
          print("\nEl area del circulo es: ", area_circulo(num1), "\n")
 
#Área poligono       
     elif menu_area == 8:
        num1 = float(input("Ingrese el numero de lados del poligono: "))
        num2 = float(input("Ingrese un lado del poligono: "))
        num3 = float(input("Ingrese la apotema: "))

#Comprobar que el valor sea valido
        if num1 <= 0 or num2 <= 0 or num3 <= 0:
          print("\nEl valor ingresado no es valido\n")
        else:       
          print("\nEl area del poligono es: ", area_poligono(num1,num2,num3), "\n")
      
     elif menu_area == 9:
      break
    
    else:
        print("Por favor digite una opción correcta")
  
  elif menu_principal == 3:
    break
  
  else:
    print("Por favor digite una opción correcta \n")
