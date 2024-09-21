import json

def cargar_datos(archivo):
    """Carga los datos desde un archivo JSON."""
    with open(archivo, 'r', encoding='utf-8') as f:
        return json.load(f)

def imprimir_por_deporte(datos, deporte):
    """Imprime los nombres completos de las personas que practican el deporte ingresado."""
    print(f"Personas que practican {deporte}:")
    for persona in datos.values():
        if deporte in persona['deportes']:
            print(f"{persona['nombres']} {persona['apellidos']}")

def imprimir_por_edad(datos, edad_min, edad_max):
    """Imprime los nombres completos de las personas en el rango de edad dado."""
    print(f"Personas con edad entre {edad_min} y {edad_max}:")
    for persona in datos.values():
        if edad_min <= persona['edad'] <= edad_max:
            print(f"{persona['nombres']} {persona['apellidos']}")

def main():
    archivo = 'dato.json'  
    datos = cargar_datos(archivo)

    # Solicita el deporte al usuario y muestra las personas que lo practican
    deporte_usuario = input("Ingrese el deporte: ")
    imprimir_por_deporte(datos, deporte_usuario)

    # Solicita el rango de edad al usuario y muestra las personas en ese rango
    edad_min = int(input("Ingrese la edad mínima: "))
    edad_max = int(input("Ingrese la edad máxima: "))
    imprimir_por_edad(datos, edad_min, edad_max)

if __name__ == "__main__":
    main()