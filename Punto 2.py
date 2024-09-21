def mezclar_diccionarios(dic1, dic2):
    # Copiar el primer diccionario para no modificar los originales
    dic_combinado = dic1.copy()

    # Añadir las claves y valores del segundo diccionario solo si no están en el primero
    for clave, valor in dic2.items():
        if clave not in dic_combinado:
            dic_combinado[clave] = valor

    return dic_combinado

# Ejemplo de uso
dic1 = {'a': 1, 'b': 2, 'c': 3}
dic2 = {'b': 4, 'd': 5}

resultado = mezclar_diccionarios(dic1, dic2)
print(resultado)