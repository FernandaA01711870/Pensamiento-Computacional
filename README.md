
# Calculadora de perímetros y áreas

Mientras buscaba un proyecto para realizar en Python 3 la primera cosa que me vino a la mente fue la típica calculadora, pero en proyectos anteriores de programación siempre había realizado calculadoras así que esta vez decidí hacer un pequeño cambio y subir un poco de nivel haciendo una calculadora que nos permita calcular el perímetro y área de una figura.

Me parece que será bastante útil e interesante de diseñar.

**Funcionará de la siguiente manera:**

El usuario proporcionara el nombre de la figura.
Para el perímetro se le pedirá que proporcione la longitud de los lados.
Y para el área dependiendo de la figura se usara la fórmula para dicha figura geométrica, en el caso del círculo se le pedirá que ingrese el valor del radio.
## Algoritmo
1.     Mostrar un mensaje de bienvenida al usuario
			print("Bienvenido a su calculadora de áreas y perímetros\n")
2.     Desplegar un menú con las opciones con las cuales contara el usuario (perímetro, área o salir del programa).
			menu_principal  =  int(input("1- Perímetros 2- Áreas 3- Salir"))
3.     Si el usuario elije la opción de perímetros se desplegará otro menú con los nombres de las figuras que podrá consultar para saber su perímetro.
			if menu_principal == 1: 
				menu_perimetro = int(input("1-Cuadrado 2-Triangulo 3-Rectangulo 4-Paralelogramo 5-Rombo 6-Trapecio 7-Circulo 8-Poligono Regular 9-Salir "))

4.     Dependiendo de la opción que el usuario elija se calculara el perímetro de la figura mediante la formula correspondiente y con los datos que el usuario ingrese.

			if menu_perimetro == 1:
					a = float(input("Ingrese un lado del cuadrado: "))
					p_cuadrado = a * 4
					print("El perimetro del cuadrado es: ", p_cuadrado)
					
			elif menu_perimetro == 2:
					a = float(input("Ingrese un lado del triangulo: "))
					b = float(input("Ingrese el segundo lado del triangulo: "))
					c = float(input("Ingrese el tercer lado del triangulo :"))
					p_triangulo = a + b + c
					print("El perimetro del triangulo es: ", p_triangulo)
					
			elif menu_perimetro == 3:
					a = float(input("Ingrese la altura del rectangulo: "))
					b = float(input("Ingrese la base del rectangulo: "))
					p_rectangulo = 2*(b * a)
					print("El perimetro del rectangulo es: ", p_rectangulo)
					
			elif menu_perimetro == 4:
					a = float(input("Ingrese la altura del paralelogramo: "))
					b = float(input("Ingrese la base del paralelogramo: "))
					p_paralelogramo = 2*(b * a)
					print("El perimetro del paralelogramo es: ", p_paralelogramo)
					
			elif menu_perimetro == 5:
					a = float(input("Ingrese un lado del rombo: "))
					p_rombo = 4*a
					print("El perimetro del rombo es: ", p_rombo)
					
			elif menu_perimetro == 6:
					B = float(input("Ingrese la altura mayor del trapecio: "))
					b = float(input("Ingrese la altura menor del trapecio: "))
					a = float(input("Ingrese un lado del trapecio: "))
					c = float(input("Ingrese el segundo lado del trapecio: "))
					p_trapecio = B + b + a + c
					print("El perimetro del trapecio es: ", p_trapecio)
					
			elif menu_perimetro == 7:
					r = float(input("Ingrese el radio del circulo: "))
					PI = 3.1416
					p_circulo = 2 * PI * r
					print("El perimetro del circulo es: ", p_circulo)
					
			elif menu_perimetro == 8:
					n = float(input("Ingrese el numero de lados del poligono: "))
					b = float(input("Ingrese un lado del poligono: "))
					p_poligono = n*b
					print("El perimetro del poligono es: ", p_poligono)
					
			else:
					print("Por favor digite una opción correcta")
5.     Por otro lado si el usuario elije la opción de áreas se desplegará otro menú con los nombres de las figuras que podrá consultar para conocer su área.
			elif menu_principal == 2:
					menu_area = int(input("1-Cuadrado 2-Triangulo 3-Rectangulo 4-Paralelogramo 5-Rombo 6-Trapecio 7-Circulo 8-Poligono Regular 9-Salir"))

6.     Dependiendo de la opción que el usuario elija se calculara el área de la figura mediante la formula correspondiente y con los datos que el usuario ingrese.
			if menu_area == 1:
					a = float(input("Ingrese un lado del cuadrado: "))
					a_cuadrado = a ** 2
					print("El area del cuadrado es: ", a_cuadrado, "\n")

			elif menu_area == 2:
					b = float(input("Ingrese la base del triangulo: "))
					h = float(input("Ingrese la altura del triangulo :"))
					a_triangulo = b * h / 2
					print("El área del triangulo es: ", a_triangulo)

			elif menu_area == 3:
					a = float(input("Ingrese la altura del rectangulo: "))
					b = float(input("Ingrese la base del rectangulo: "))
					a_rectangulo = b * a
					print("El área del rectangulo es: ", a_rectangulo)

			elif menu_area == 4:
					h = float(input("Ingrese la altura (h) del paralelogramo: "))
					b = float(input("Ingrese la base del paralelogramo: "))
					a_paralelogramo = b * h
					print("El área del paralelogramo es: ", a_paralelogramo)

			elif menu_area == 5:
					D = float(input("Ingrese la diagonal mayor del rombo: "))
					d = float(input("Ingrese la diagonal menor del rombo: "))
					a_rombo = D*d/2
					print("El área del rombo es: ", a_rombo)

			elif menu_area == 6:
					B = float(input("Ingrese la base mayor : "))
					b = float(input("Ingrese la base menor: "))
					h = float(input("Ingrese la altura (h): "))
					a_trapecio = (B * b)/2
					print("El área del trapecio es: ", a_trapecio)

			elif menu_area == 7:
					r = float(input("Ingrese el radio del circulo: "))
					PI = 3.1416
					a_circulo = PI * r**2
					print("El área del circulo es: ", a_circulo)

			elif menu_area == 8:
					n = float(input("Ingrese el numero de lados del poligono: "))
					b = float(input("Ingrese un lado del poligono: "))
					a = float(input("Ingrese la apotema: "))
					a_poligono = (n*b)*a/2
					print("El área del polígono es: ", a_poligono)

			else:
					print("Por favor digite una opción correcta")

7.     Finalmente si el usuario digita la opción de salir el programa dejara se ejecutarse 
			elif menu_principal == 3:
				break

# Implementación de matrices en el código

Para esta entrega del proyecto desarrollado en Python, he tomado la decisión de no implementar el uso de matrices en el código. Mi proyecto se centra en el desarrollo de una calculadora que permite calcular el área y perímetro de diversas figuras geométricas, como cuadrados, triángulos, rectángulos, paralelogramos, rombos, trapecios, círculos y polígonos regulares.

A pesar de que el proyecto pueda parecer una tarea sencilla en su naturaleza, me ha brindado la oportunidad de integrar de manera exitosa todos los temas que hemos abordado hasta el momento en nuestro curso. Cada concepto ha sido aplicado con precisión y cuidado siguiendo las reglas establecidas en la materia, con el objetivo de mejorar el funcionamiento y mantener mi cogido legible y comprensible. Mi enfoque ha sido la eficacia y la claridad en la implementación y no únicamente integrar características complejas y es por esta razón que he llegado a la conclusión de no incorporar elementos adicionales en el código.

# Correcciones finales

1.- README - algoritmo

Me gustaría que volviera a revisar el README la parte del algoritmo fue corregido, se agregaron las correcciones y observaciones que me realizó.

2.- Uso de listas

En el apartado del avance 6 y 7 del uso de listas se marco como incompleto ya que se dice que hago mención de la lista pero no la utilizo sin embargo esta lista es utilizada para el menú y es llamada en la función 'main' para cumplir su objetivo de menú. Y sobre la mención de solo usar un uso único de listas, este fue un tema que hable con usted en clase y me dijo que el uso de la lista era correcto.

Por el momento es todo, gracias :D

