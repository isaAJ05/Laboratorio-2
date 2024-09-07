# POR: Isabella Arrieta y Paula Núñez

from itertools import product

def extraer_variables(proposicion):
    # Filtra las letras del alfabeto en la proposición, elimina duplicados y ordena caracteres
    return sorted(set(filter(str.isalpha, proposicion)))

def generar_combinaciones(variables):
    #productoria de repeticiones de True y False de acuerdo a la cantidad de variables y se convierte en lista de tuplas
    return list(product([True, False], repeat=len(variables)))

def evaluar_proposicion(proposicion, valores_verdad):
    # Reemplazar las variables en la proposición con sus valores de verdad
    nueva_proposicion = ""
    i = 0
    while i < len(proposicion):
        if proposicion[i].isalpha():  # Si es una variable
            variable = proposicion[i]
            if variable in valores_verdad:
                nueva_proposicion += str(valores_verdad[variable]) # Reemplazar por su valor de verdad
            else:
                nueva_proposicion += variable # Mantener la variable si no tiene valor de verdad
        # Reemplazar los operadores lógicos por sus equivalentes en Python
        elif proposicion[i] == '¬': # NOT
            nueva_proposicion += ' not '
        elif proposicion[i] == '&': # AND
            nueva_proposicion += ' and '
        elif proposicion[i] == '|': # OR
            nueva_proposicion += ' or '
        elif proposicion[i:i+2] == '->': # ENTONCES
            nueva_proposicion += ' <= '
            i += 1  # Saltar el siguiente carácter '>'
        elif proposicion[i:i+3] == '<->': # SI Y SOLO SI
            nueva_proposicion += ' == '
            i += 2  # Saltar los siguientes dos caracteres '->'
        else:
            nueva_proposicion += proposicion[i]
        i += 1
    
    return eval(nueva_proposicion) # Evaluar la expresión como código Python

# Función para verificar si dos proposiciones son equivalentes
def verificar_equivalencia(proposicion1, proposicion2):
    variables = sorted(set(extraer_variables(proposicion1) + extraer_variables(proposicion2))) # Unión de variables
    combinaciones = generar_combinaciones(variables)
    
    for combinacion in combinaciones:
        valores_verdad = dict(zip(variables, combinacion)) # Se crea un diccionario de valores de verdad
        resultado1 = evaluar_proposicion(proposicion1, valores_verdad)
        resultado2 = evaluar_proposicion(proposicion2, valores_verdad)
        if resultado1 != resultado2:
            return False, valores_verdad # Se encontró una diferencia en los valores de verdad
    
    return True, None # No se encontraron diferencias en los valores de verdad

 # Imprimir la tabla de verdad en consola
def imprimir_tabla_verdad(proposicion1, proposicion2):
    variables = sorted(set(extraer_variables(proposicion1) + extraer_variables(proposicion2))) # Unión de variables
    combinaciones = generar_combinaciones(variables)
    
    # Encabezado de la tabla
    encabezado = "\t".join(variables) + "\t" + "Proposición 1" + "\t" + "Proposición 2"
    print(f"\nTabla de verdad:\n {encabezado} \n---------------------------------------------")
    
    for combinacion in combinaciones:
        valores_verdad = dict(zip(variables, combinacion)) # Diccionario de valores de verdad
        resultado1 = evaluar_proposicion(proposicion1, valores_verdad)  # Se evaluan todos los posibles resultados de la proposición 1
        resultado2 = evaluar_proposicion(proposicion2, valores_verdad) # Se evaluan todos los posibles resultados de la proposición 2
        tabla_de_verdad = "\t".join(map(str, combinacion)) + "\t    " + str(resultado1) + "\t    " + str(resultado2)
        print(tabla_de_verdad)   


print("¡Bienvenidx al verificador de equivalencia de proposiciones lógicas!")
# Ciclo para poder hacer múltiples verificaciones en una sola ejecución
while True:
    # Ingreso de proposiciones
    proposicion1 = input("\nIngrese la primera proposición: ")
    proposicion2 = input("Ingrese la segunda proposición: ")

    imprimir_tabla_verdad(proposicion1, proposicion2)# Imprimir la tabla de verdad
    equivalentes, valores_verdad = verificar_equivalencia(proposicion1, proposicion2) 

    # Devolver un mensaje indicando si las proposiciones son equivalentes o no.
    if equivalentes:
        print("\nLas proposiciones son equivalentes :)")
    else:
        print("\nLas proposiciones no son equivalentes :(")
        print(f"Primera diferencia encontrada entre los valores de verdad: {valores_verdad}")

    # Preguntar al usuario si desea continuar
    while True:
        continuar = input("¿Desea verificar otra equivalencia? (s/n): ").strip().lower()
        if continuar == 'n':
            print("Gracias por usar el verificador de equivalencia de proposiciones lógicas. ¡Adiós!")
            exit()
        elif continuar == 's':
            break
        else:
            print("(!) Por favor, ingrese una respuesta válida.")
