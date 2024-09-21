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
