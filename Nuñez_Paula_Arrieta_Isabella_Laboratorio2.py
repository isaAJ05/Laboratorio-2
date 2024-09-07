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
        elif proposicion[i] == '¬':
            nueva_proposicion += ' not '
        elif proposicion[i] == '&':
            nueva_proposicion += ' and '
        elif proposicion[i] == '|':
            nueva_proposicion += ' or '
        elif proposicion[i:i+2] == '->':
            nueva_proposicion += ' <= '
            i += 1  # Saltar el siguiente carácter '>'
        else:
            nueva_proposicion += proposicion[i]
        i += 1
    
    return eval(nueva_proposicion) # Evaluar la expresión como código Python

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

# Ingreso de proposiciones
print("Bienvenido al verificador de equivalencia de proposiciones lógicas")
proposicion1 = input("Ingrese la primera proposición: ")
proposicion2 = input("Ingrese la segunda proposición: ")

equivalentes, valores_verdad = verificar_equivalencia(proposicion1, proposicion2)

if equivalentes:
    print("\nLas proposiciones son equivalentes :)")
else:
    print("\nLas proposiciones no son equivalentes :( )")
    print(f"Diferencia encontrada con los valores de verdad: {valores_verdad}")