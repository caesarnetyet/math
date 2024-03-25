import sympy as sp

print("Bienvenido al programa de resolución de ecuaciones diferenciales.")
print("Este programa resuelve ecuaciones diferenciales de la forma: y'' + p(x)y' + q(x)y = f(x)")


def validar_numero(entrada):
    while True:
        valor = input(entrada)
        try:
            valor_numerico = int(valor)
            return valor_numerico
        except ValueError:
            print("Error: Ingresa solo números enteros.")

#coeficiente_ydoble = validar_numero("Ingresa el coeficiente de y'' (deja en blanco si es 1): ")
coeficiente_yprima = validar_numero("Ingresa el coeficiente de y' (deja en blanco si es 0): ")
coeficiente_independiente = validar_numero("Ingresa el coeficiente independiente (deja en blanco si es 0): ")
coeficiente_xcuadrado = validar_numero("Ingresa el coeficiente de x² (deja en blanco si es 0): ")
coeficiente_x = validar_numero("Ingresa el coeficiente de x (deja en blanco si es 0): ")
termino_independiente = validar_numero("Ingresa el término independiente (deja en blanco si es 0): ")

# Definimos las variables y los coeficientes de la ecuación cuadrática
x = sp.Symbol('x')
a = 1
#primer termino
b = coeficiente_yprima
#segundo termino
c = coeficiente_independiente
#================================
d = coeficiente_xcuadrado

e = coeficiente_x

f = termino_independiente


print(f"ECUACION")
print(f"y'' + {b}y' + {c} = {d}x² + {e}x + {f}")
# Creamos la ecuación cuadrática
ecuacion = a*x**2 + b*x + c

# Calculamos las raíces de la ecuación cuadrática
raices = sp.solve(ecuacion, x)

# Mostramos las raíces calculadas y las guardamos en variables separadas
print("Factorizacion:")
x1 = raices[0].evalf()
x2 = raices[1].evalf()

print(f"x1 = {x1}")
print(f"x2 = {x2}")
##############################################################################################################
# Definimos las variables y las expresiones generales
x, A, B, C = sp.symbols('x A B C')
Yp = A*x**2 + B*x + C
Yp_prime = 2*A*x + B
Yp_double_prime = 2*A

# Definimos los coeficientes que acompañan a las expresiones generales
coef_yp_double_prime = 1
coef_yp_prime = b
coef_y = c

# Sustituimos las expresiones generales en la ecuación original
ecuacion = coef_yp_double_prime*Yp_double_prime + coef_yp_prime*Yp_prime + coef_y*Yp

# Mostramos la ecuación resultante
print("La ecuación resultante es:")
print(sp.latex(ecuacion))


# Separamos los términos que contienen x^2 y despejamos A
termino_x2 = ecuacion.coeff(x**2)
ecuacion_simplificada = sp.Eq(termino_x2, d)  # Igualamos el término a 2
A_valor = sp.solve(ecuacion_simplificada, A)[0]

# Mostramos los resultados
print("\nX² ->:")
print(A_valor)





# Separamos los términos que contienen x y despejamos B
termino_x = ecuacion.coeff(x)
ecuacion_simplificada_x = sp.Eq(termino_x, e)  # Igualamos el término a 7
B_valor = sp.solve(ecuacion_simplificada_x.subs(A, A_valor), B)[0]

# Mostramos los resultados
print("\nX ->")
print(B_valor)


# Separamos el término independiente y despejamos C
termino_independiente = ecuacion - termino_x2*x**2 - termino_x*x
ecuacion_simplificada_ind = sp.Eq(termino_independiente, f)  # Igualamos el término al valor independiente
C_valor = sp.solve(ecuacion_simplificada_ind.subs({A: A_valor, B: B_valor}), C)[0]


print("\nInd ->")
print(C_valor)


print("\nRESULTADO")
print(f"C₁e{x1}ˣ + C₂e{x2}ˣ + ({A_valor})X² + ({B_valor})X + {C_valor}")