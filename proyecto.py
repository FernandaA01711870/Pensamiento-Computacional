#Mostrar un mensaje de bienvenida al usuario

print("Bienvenido a su calculadora de áreas y perímetros\n")

print("Indique si quiere calcular perimetros o áreas: \n") 

"""En esta parte de deslegara un menu por el cual el usuario podra escoger entre calcular perímetro o area de una figura"""

menu_principal = int(input("1- Perimetros\n2- Áreas\n3- Salir\n\n"))

while menu_principal != 3:
  
  if menu_principal == 1:  #Calcular perimetros
    print("Bienvenido al menú de perimetros\n")
    print("Indique de que figura le gustaria conocer su perimetro\n")

    menu_perimetro = int(input("1- Cuadrado\n2- Triangulo\n3- Rectangulo\n4- Paralelogramo\n5- Rombo \n6- Trapecio\n7- Circulo\n8- Poligono Regular\n9- Salir\n"))

    while menu_perimetro != 9:
    
      if menu_perimetro == 1:
       a = float(input("Ingrese un lado del cuadrado: "))
       p_cuadrado = a * 4
       print("El perimetro del cuadrado es: ", p_cuadrado, "\n")

       break
        
      elif menu_perimetro == 2:
        a = float(input("Ingrese un lado del triangulo: "))
        b = float(input("Ingrese el segundo lado del triangulo: "))
        c = float(input("Ingrese el tercer lado del triangulo :"))

        p_triangulo = a + b + c

        print("El perimetro del triangulo es: ", p_triangulo, "\n")

        break
      
      elif menu_perimetro == 3:
        a = float(input("Ingrese la altura del rectangulo: "))
        b = float(input("Ingrese la base del rectangulo: "))
        
        p_rectangulo = 2*(b * a)
        
        print("El perimetro del rectangulo es: ", p_rectangulo, "\n")

        break
        
      elif menu_perimetro == 4:
        a = float(input("Ingrese la altura del paralelogramo: "))
        b = float(input("Ingrese la base del paralelogramo: "))
        
        p_paralelogramo = 2*(b * a)
        
        print("El perimetro del paralelogramo es: ", p_paralelogramo, "\n")

        break
        
      elif menu_perimetro == 5:
        a = float(input("Ingrese un lado del rombo: "))
        
        p_rombo = 4*a
        
        print("El perimetro del rombo es: ", p_rombo, "\n")

        break
        
      elif menu_perimetro == 6:
        B = float(input("Ingrese la altura mayor del trapecio: "))
        b = float(input("Ingrese la altura menor del trapecio: "))
        a = float(input("Ingrese un lado del trapecio: "))
        c = float(input("Ingrese el segundo lado del trapecio: "))
        p_trapecio = B + b + a + c
        
        print("El perimetro del trapecio es: ", p_trapecio, "\n")

        break
      
      elif menu_perimetro == 7:
        r = float(input("Ingrese el radio del circulo: "))

        PI = 3.1416
        p_circulo = 2 * PI * r
        
        print("El perimetro del circulo es: ", p_circulo, "\n")

        break
        
      elif menu_perimetro == 8:
        n = float(input("Ingrese el numero de lados del poligono: "))
        b = float(input("Ingrese un lado del poligono: "))
        
        p_poligono = n*b
        
        print("El perimetro del poligono es: ", p_poligono, "\n")
        
        break
        
      else:
        
        print("Por favor digite una opción correcta")

      break
      
    break
    
  elif menu_principal == 2:
    print("Bienvenido al menú de áreas\n")
    print("Indique de que figura le gustaria conocer su área\n")

    menu_area = int(input("1- Cuadrado\n2- Triangulo\n3- Rectangulo\n4- Paralelogramo\n5- Rombo \n6- Trapecio\n7- Circulo\n8- Poligono Regular \n9- Salir \n\n"))

    while menu_area != 9:

      if menu_area == 1:
       a = float(input("Ingrese un lado del cuadrado: "))
       a_cuadrado = a ** 2
       print("El area del cuadrado es: ", a_cuadrado, "\n")

       break
        
      elif menu_area == 2:
        b = float(input("Ingrese la base del triangulo: "))
        h = float(input("Ingrese la altura del triangulo :"))

        a_triangulo = b * h / 2

        print("El area del triangulo es: ", a_triangulo, "\n")

        break
      
      elif menu_area == 3:
        a = float(input("Ingrese la altura del rectangulo: "))
        b = float(input("Ingrese la base del rectangulo: "))
        
        a_rectangulo = b * a
        
        print("El area del rectangulo es: ", a_rectangulo, "\n")

        break
        
      elif menu_area == 4:
        h = float(input("Ingrese la altura (h) del paralelogramo: "))
        b = float(input("Ingrese la base del paralelogramo: "))
        
        a_paralelogramo = b * h
        
        print("El perimetro del paralelogramo es: ", a_paralelogramo, "\n")

        break
        
      elif menu_area == 5:
        D = float(input("Ingrese la diagonal mayor del rombo: "))
        d = float(input("Ingrese la diagonal menor del rombo: "))
        
        a_rombo = D*d/2
        
        print("El perimetro del rombo es: ", a_rombo, "\n")

        break
        
      elif menu_area == 6:
        B = float(input("Ingrese la base mayor : "))
        b = float(input("Ingrese la base menor: "))
        h = float(input("Ingrese la altura (h): "))
        a_trapecio = (B * b)/2
        
        print("El perimetro del trapecio es: ", a_trapecio, "\n")

        break
    
      elif menu_area == 7:
        r = float(input("Ingrese el radio del circulo: "))
        
        PI = 3.1416
        a_circulo = PI * r**2
        
        print("El perimetro del circulo es: ", a_circulo, "\n")

        break
        
      elif menu_area == 8:
        n = float(input("Ingrese el numero de lados del poligono: "))
        b = float(input("Ingrese un lado del poligono: "))
        a = float(input("Ingrese la apotema: "))
        
        a_poligono = (n*b)*a/2
        
        print("El perimetro del poligono es: ", a_poligono, "\n")
        
        break
        
      else:
        
        print("Por favor digite una opción correcta")

      break
      
    break
     
  else:
    print("Por favor digite una opción correcta")
    break
