# imprimir , si coloco la f anteponiendola significa que voy a formatear el string
Nombre = "Pablo Calvano"
print(f'Hola {str(Nombre)}')

# formatear strings


# Trabajando con Arreglos  [0, 1, 2, ...]
array = ['Colombia', 'Puerto Rico', 'Costa Rica', 'Argentina']

array.append('Bolivia')

print(array)
# print (array[4])

i = 0
for pais in array:
    print(pais)

    if pais == 'Argentina':
        print(f'{Nombre}, vive en {pais}')
        #break       # romper cob el loop
        continue     # pasa al siguiente elemento

    if pais == 'Costa Rica':
        array[i] = "Aguante los Ticos"
        print(array[i])
        continue

    if pais == 'Bolivia':
        print (f'{Nombre}, vive en {pais}')
        break

i++1

        #continue   # pasa a siguiente elemento

# Validar = isinstance(array, list)

# trabajando con diccionarios , permiten identificar cada elemento con una key = EJEMPLO: "  'nombre' : 'Carlos' , 'edad' : 28,  'cursos' : ['Python' , 'Django' , 'JS']
diccionario = {'nombre' : 'Pablo' , 'edad' : 34,  'cursos' : ['Python' , 'Django' , 'JS'] }

# EJEMPLO
Nombre = diccionario['nombre'] # accedo al valor del diccionario mediante la key nombre , EJEMPLO = un JSON de una Response

print (f'Hola {Nombre}!')

# acess_token = dicc['access_token']

# Validar = isinstance(dicc, dict)
