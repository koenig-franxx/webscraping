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
            nombre = onclick_text.split("'")[1]
            dificultad = onclick_text.split("'")[3]
            autor = onclick_text.split("'")[7]
            maquinas_info.append((nombre, dificultad, autor))

        return maquinas_info
    else:
        raise Exception(f"Error al realizar la petición: {respuesta.status_code}")

def contar_maquinas(maquinas_info):
    """Cuenta la cantidad de máquinas encontradas"""
    return len(maquinas_info)

