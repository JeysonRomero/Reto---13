# Reto---13

### Punto 1 /Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.
```py

mi_diccionario = {'a': 3, 'b': 1, 'c': 2, 'd': 5}

valores = list(mi_diccionario.values())

# Ordenar los valores en forma ascendente
valores_ordenados = sorted(valores)

# Imprimir los valores ordenados
print("Valores del diccionario en orden ascendente:", valores_ordenados)
```

### Punto 2 /Desarrollar una funci�on que reciba dos diccionarios como par�ametros y los mezcle, es decir, que se construya un nuevo diccionario con las llaves de los dos diccionarios; si hay una clave repetida en ambos diccionarios, se debe asignar el valor que tenga la clave en el primer diccionario.

```py
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
```


### Punto 3 /Dado el JSON:

```py
{
	"jadiazcoronado":{
		"nombres": "Juan Antonio",
		"apellidos": "D��az Coronado",
		"edad":19,
		"colombiano":true,
		"deportes":["F�utbol","Ajedrez","Gimnasia"]
	},
	"dmlunasol":{
		"nombres": "Dorotea Maritza",
		"apellidos": "Luna Sol",
		"edad":25,
		"colombiano":false,
		"deportes":["Baloncesto","Ajedrez","Gimnasia"]
	}
}
```

## Cree un programa que lea de un archivo con dicho JSON y:

### - Imprima los nombres completos (nombre y apellidos) de las personas que practican el deporte ingresado por el usuario.

### - Imprima los nombres completos (nombre y apellidos) de las personas que est�en en un rango de edades dado por el usuario.

```py
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
```

El código en Python está diseñado para trabajar con un archivo dato.json que contiene información sobre personas en formato JSON. Primero, el programa carga los datos del archivo utilizando la función cargar_datos. Luego, solicita al usuario que ingrese un deporte y un rango de edades. Utilizando la función imprimir_por_deporte, el programa busca e imprime los nombres completos de las personas que practican el deporte especificado. De manera similar, la función imprimir_por_edad filtra y muestra los nombres completos de las personas cuya edad está dentro del rango dado. El archivo JSON debe estar correctamente formateado, con cada persona representada como un diccionario con campos como nombres, apellidos, edad y una lista de deportes.

### Punto 4 /El siguiente código contiene un JSON con el pronostivo detallado del clima para 8 días:


```py
import json

# Cargar archivo
jsonString = '''
{\"dt\": {\"0\": 1685116800, \"1\": 1685203200, \"2\": 1685289600, \"3\": 1685376000, \"4\": 1685462400, \"5\": 1685548800, \"6\": 1685635200, \"7\": 1685721600}, \"sunrise\": {\"0\": 1685097348, \"1\": 1685183745, \"2\": 1685270143, \"3\": 1685356542, \"4\": 1685442942, \"5\": 1685529342, \"6\": 1685615743, \"7\": 1685702145}, \"sunset\": {\"0\": 1685143042, \"1\": 1685229458, \"2\": 1685315875, \"3\": 1685402291, \"4\": 1685488708, \"5\": 1685575124, \"6\": 1685661541, \"7\": 1685747958}, \"moonrise\": {\"0\": 1685118300, \"1\": 1685207460, \"2\": 1685296620, \"3\": 1685385720, \"4\": 1685474880, \"5\": 1685564220, \"6\": 1685653740, \"7\": 1685743500}, \"moonset\": {\"0\": 0, \"1\": 1685164320, \"2\": 1685253000, \"3\": 1685341560, \"4\": 1685430120, \"5\": 1685518740, \"6\": 1685607600, \"7\": 1685696640}, \"moon_phase\": {\"0\": 0.22, \"1\": 0.25, \"2\": 0.28, \"3\": 0.31, \"4\": 0.35, \"5\": 0.38, \"6\": 0.41, \"7\": 0.45}, \"pressure\": {\"0\": 1011, \"1\": 1012, \"2\": 1012, \"3\": 1012, \"4\": 1012, \"5\": 1012, \"6\": 1012, \"7\": 1011}, \"humidity\": {\"0\": 85, \"1\": 61, \"2\": 68, \"3\": 74, \"4\": 84, \"5\": 66, \"6\": 81, \"7\": 82}, \"dew_point\": {\"0\": 23.93, \"1\": 22.5, \"2\": 23.67, \"3\": 23.35, \"4\": 24.22, \"5\": 22.73, \"6\": 23.18, \"7\": 22.93}, \"velViento\": {\"0\": 3.56, \"1\": 5.07, \"2\": 5.38, \"3\": 3.95, \"4\": 4.74, \"5\": 3.75, \"6\": 4.08, \"7\": 5.94}, \"dirViento\": {\"0\": 188, \"1\": 14, \"2\": 21, \"3\": 23, \"4\": 40, \"5\": 330, \"6\": 176, \"7\": 168}, \"wind_gust\": {\"0\": 6.47, \"1\": 8.86, \"2\": 8.95, \"3\": 6.12, \"4\": 7.17, \"5\": 5.4, \"6\": 5.13, \"7\": 9.67}, \"weather\": {\"0\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"1\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"2\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"3\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"4\": [{\"id\": 501, \"main\": \"Rain\", \"description\": \"lluvia moderada\", \"icon\": \"10d\"}], \"5\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"6\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}], \"7\": [{\"id\": 500, \"main\": \"Rain\", \"description\": \"lluvia ligera\", \"icon\": \"10d\"}]}, \"clouds\": {\"0\": 100, \"1\": 82, \"2\": 99, \"3\": 100, \"4\": 100, \"5\": 59, \"6\": 100, \"7\": 100}, \"pop\": {\"0\": 1.0, \"1\": 0.65, \"2\": 0.98, \"3\": 0.86, \"4\": 1.0, \"5\": 0.62, \"6\": 0.93, \"7\": 0.95}, \"prcp\": {\"0\": 40.0, \"1\": 1.65, \"2\": 14.01, \"3\": 5.07, \"4\": 16.55, \"5\": 2.17, \"6\": 2.77, \"7\": 1.73}, \"uvi\": {\"0\": 10.14, \"1\": 12.78, \"2\": 12.73, \"3\": 8.44, \"4\": 0.59, \"5\": 1.0, \"6\": 1.0, \"7\": 1.0}, \"temp.day\": {\"0\": 26.62, \"1\": 30.95, \"2\": 30.17, \"3\": 28.37, \"4\": 27.22, \"5\": 29.78, \"6\": 26.83, \"7\": 26.36}, \"tmpMin\": {\"0\": 25.64, \"1\": 24.64, \"2\": 25.84, \"3\": 25.56, \"4\": 25.72, \"5\": 24.86, \"6\": 25.96, \"7\": 25.47}, \"tmpMax\": {\"0\": 27.16, \"1\": 31.1, \"2\": 30.2, \"3\": 29.5, \"4\": 28.87, \"5\": 29.78, \"6\": 28.96, \"7\": 28.25}, \"temp.night\": {\"0\": 25.67, \"1\": 27.39, \"2\": 26.24, \"3\": 27.2, \"4\": 25.92, \"5\": 27.14, \"6\": 26.56, \"7\": 25.66}, \"temp.eve\": {\"0\": 25.91, \"1\": 28.73, \"2\": 27.42, \"3\": 28.27, \"4\": 27.94, \"5\": 29.29, \"6\": 28.96, \"7\": 28.12}, \"temp.morn\": {\"0\": 26.5, \"1\": 24.64, \"2\": 26.13, \"3\": 25.72, \"4\": 26.04, \"5\": 24.86, \"6\": 25.98, \"7\": 25.57}, \"feels_like.day\": {\"0\": 26.62, \"1\": 34.99, \"2\": 34.96, \"3\": 32.03, \"4\": 30.67, \"5\": 33.62, \"6\": 29.45, \"7\": 26.36}, \"feels_like.night\": {\"0\": 26.56, \"1\": 30.98, \"2\": 26.24, \"3\": 30.62, \"4\": 26.84, \"5\": 30.16, \"6\": 26.56, \"7\": 26.45}, \"feels_like.eve\": {\"0\": 26.85, \"1\": 32.49, \"2\": 30.94, \"3\": 31.8, \"4\": 31.51, \"5\": 33.17, \"6\": 32.64, \"7\": 31.18}, \"feels_like.morn\": {\"0\": 26.5, \"1\": 25.48, \"2\": 26.13, \"3\": 26.62, \"4\": 26.04, \"5\": 25.73, \"6\": 25.98, \"7\": 26.4}, \"date\": {\"0\": 1685098800000, \"1\": 1685185200000, \"2\": 1685271600000, \"3\": 1685358000000, \"4\": 1685444400000, \"5\": 1685530800000, \"6\": 1685617200000, \"7\": 1685703600000}, \"main\": {\"0\": \"Rain\", \"1\": \"Rain\", \"2\": \"Rain\", \"3\": \"Rain\", \"4\": \"Rain\", \"5\": \"Rain\", \"6\": \"Rain\", \"7\": \"Rain\"}, \"description\": {\"0\": \"lluvia moderada\", \"1\": \"lluvia ligera\", \"2\": \"lluvia moderada\", \"3\": \"lluvia ligera\", \"4\": \"lluvia moderada\", \"5\": \"lluvia ligera\", \"6\": \"lluvia ligera\", \"7\": \"lluvia ligera\"}, \"icono\": {\"0\": \"10d\", \"1\": \"10d\", \"2\": \"10d\", \"3\": \"10d\", \"4\": \"10d\", \"5\": \"10d\", \"6\": \"10d\", \"7\": \"10d\"}, \"alertPrecip\": {\"0\": \"X\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertAlertas\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertVelViento\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"X\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMax\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"X\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMin\": {\"0\": \"-\", \"1\": \"X\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"recomendaciones\": {\"lluvias\": \"Realice una revisi\\u00f3n y limpieza a la red de desague y canales existentes ENTER8 Cuente con una estaci\\u00f3n de bombeo, que debe estar ubicada en el punto m\\u00e1s bajo del predio. Aseg\\u00farese de encender y probar el sistema de bombeo al menos una vez al mes y hacer un mantenimiento mensual al equipo de bombeoENTER8 Los productos alojados en zonas de almacenamiento deben mantenersen sobre estibas - estanterias, con el fin de que no entren en contacto directo con el agua.\", \"vientos\": \"-\", \"temperatura\": \"-\"}}
'''
data = json.loads(jsonString)

```

Revise los campos: 'alertAlertas', 'alertPrecip', 'alertTmpMax', 'alertTmpMin', 'alertVelViento'. Para cada uno identifique si se presentan alertas ({0: x} indica que el día 0 habra un fenomeno de la alerta en cuestión, {1:"-"} indica que no habrá ningun fenomeno climatico). En caso que se presente una alerta obtenga la fecha del campo 'dt' (aquí pueden revisar como se convierte de UTC a fecha), así como los parametros relevantes del evento (e.g. si es un fenomeno de lluvias, busqye el nivel de lluvia, si es vientos, la velocidad del viuento). Al final deberá imprimir las fechas de alerta, el tipo de alerta y las variables asociadas.


```py
import json
from datetime import datetime, timezone

# Función para convertir fecha legible a timestamp
def convert_date_to_timestamp(date_str):
    return int(datetime.strptime(date_str, '%Y-%m-%d').replace(tzinfo=timezone.utc).timestamp())

# Cargar el archivo JSON (actualiza aquí con datos verdaderos)
jsonString = '''
{
    "dt": {"0": 1726704000, "1": 1726790400, "2": 1726876800, "3": 1726963200, "4": 1727049600, "5": 1727136000, "6": 1727222400, "7": 1727308800},
    "alertPrecip": {"0": "X", "1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-"},
    "alertVelViento": {"0": "-", "1": "-", "2": "X", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-"},
    "alertTmpMax": {"0": "-", "1": "-", "2": "-", "3": "-", "4": "-", "5": "X", "6": "-", "7": "-"},
    "alertTmpMin": {"0": "-", "1": "X", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-"},
    "velViento": {"0": 10.5, "1": 5.0, "2": 15.3, "3": 7.8, "4": 6.1, "5": 12.4, "6": 8.9, "7": 4.5},
    "prcp": {"0": 25.0, "1": 0.0, "2": 10.0, "3": 5.5, "4": 20.0, "5": 30.0, "6": 15.0, "7": 2.5}
}
'''

data = json.loads(jsonString)

# Función para convertir timestamp a fecha
def convert_timestamp_to_date(timestamp):
    return datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime('%Y-%m-%d')

# Revisar alertas
alertas = {
    "alertPrecip": ("nivel de lluvia", 'prcp'),
    "alertVelViento": ("velocidad del viento", 'velViento'),
    "alertTmpMax": ("temperatura máxima", None),
    "alertTmpMin": ("temperatura mínima", None)
}

# Almacenar resultados
resultados_alertas = []

for alert_type, (description, variable_key) in alertas.items():
    for day, alert in data[alert_type].items():
        if alert == 'X':
            fecha = convert_timestamp_to_date(data['dt'][day])
            if variable_key:
                variable = data[variable_key][day]
                resultados_alertas.append(f"Fecha: {fecha}, Tipo de alerta: {description}, Variable: {variable} {'mm' if variable_key == 'prcp' else 'm/s'}")
            else:
                resultados_alertas.append(f"Fecha: {fecha}, Tipo de alerta: {description}")

# Imprimir resultados
for resultado in resultados_alertas:
    print(resultado)


```

### Punto 4/A través de un programa conectese a al menos 3 API's , obtenga el JSON, imprimalo y extraiga los pares de llave : valor.
