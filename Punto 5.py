import requests

apis = [
    "https://catfact.ninja/fact",
    "https://api.coindesk.com/v1/bpi/currentprice.json",
    "https://official-joke-api.appspot.com/random_joke"
]


def fetch_and_print_json(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        json_data = response.json()
        
        print(f"Datos de {api_url}:")
        print(json_data)
        
        print("\nPares llave: valor:")
        for key, value in json_data.items():
            print(f"{key}: {value}")
        print("\n" + "="*50 + "\n")

    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud a {api_url}: {e}")

for api in apis:
    fetch_and_print_json(api)
