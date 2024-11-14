# test_scraping.py
import pytest
from unittest.mock import patch
from script import obtener_maquinas

# Define la respuesta simulada con el formato esperado en 'onclick'
mock_respuesta = {
    "status_code": 200,
    "text": """
        <html>
            <body>
                <div onclick="onclick('Machine1', 'hard', '', '', '', '', '', 'author1')">Machine1</div>
                <div onclick="onclick('Machine2', 'medium', '', '', '', '', '', 'author2')">Machine2</div>
            </body>
        </html>
    """
}

@patch('requests.get')
def test_obtener_maquinas(mock_get):
    # Simula la respuesta de requests.get
    mock_get.return_value.status_code = mock_respuesta["status_code"]
    mock_get.return_value.text = mock_respuesta["text"]

    # Ejecuta la función
    maquinas = obtener_maquinas('https://dockerlabs.es')

    # Verifica los resultados
    assert len(maquinas) == 2
    assert maquinas[0] == ('Machine1', 'hard', 'author1')
    assert maquinas[1] == ('Machine2', 'medium', 'author2')

