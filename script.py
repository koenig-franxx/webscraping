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
            parts = onclick_text.split("'")
            
            # Verifica que hay suficientes partes antes de acceder a índices específicos
            if len(parts) > 7:
                nombre = parts[1]
                dificultad = parts[3]
                autor = parts[7]
                maquinas_info.append((nombre, dificultad, autor))
            else:
                # Si el formato es inesperado, agrega una máquina con valores 'desconocidos' o ignora
                print("Advertencia: formato inesperado en el atributo 'onclick'")
                maquinas_info.append(("Desconocido", "Desconocido", "Desconocido"))

        return maquinas_info
    else:
        raise Exception(f"Error al realizar la petición: {respuesta.status_code}")

def contar_maquinas(maquinas_info):
    """Cuenta la cantidad de máquinas encontradas"""
    return len(maquinas_info)

