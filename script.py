# script.py
import requests
from bs4 import BeautifulSoup

def obtener_maquinas(url):
    """Obtiene las máquinas desde el HTML de la página indicada"""
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        soup = BeautifulSoup(respuesta.text, 'html.parser')
        maquinas = soup.find_all('div', onclick=True)
        maquinas_info = []

        for maquina in maquinas:
            onclick_text = maquina['onclick']
            onclick_parts = onclick_text.split("'")
            
            # Verificar que el tamaño de la lista es suficiente
            nombre = onclick_parts[1] if len(onclick_parts) > 1 else 'Desconocido'
            dificultad = onclick_parts[3] if len(onclick_parts) > 3 else 'Desconocido'
            autor = onclick_parts[7] if len(onclick_parts) > 7 else 'Desconocido'

            maquinas_info.append((nombre, dificultad, autor))

        return maquinas_info
    else:
        raise Exception(f"Error al realizar la petición: {respuesta.status_code}")

