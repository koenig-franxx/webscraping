import pytest
from unittest.mock import patch
from script import obtener_maquinas, contar_maquinas

# Simulamos la respuesta de requests.get para evitar hacer una solicitud real
@pytest.fixture
def mock_respuesta():
    return {
        "status_code": 200,
        "text": """
            <html>
                <body>
                    <div onclick="someonclick('Machine1', 'hard', 'author1')">Machine1</div>
                    <div onclick="someonclick('Machine2', 'medium', 'author2')">Machine2</div>
                </body>
            </html>
        """
    }

# Test para verificar que obtener_maquinas funciona correctamente
@patch('requests.get')
def test_obtener_maquinas(mock_get, mock_respuesta):
    # Simula la respuesta de requests.get
    mock_get.return_value.status_code = mock_respuesta["status_code"]
    mock_get.return_value.text = mock_respuesta["text"]

    maquinas = obtener_maquinas('https://dockerlabs.es')
    assert len(maquinas) == 2
    assert maquinas[0] == ('Machine1', 'hard', 'author1')
    assert maquinas[1] == ('Machine2', 'medium', 'author2')

# Test para verificar la función contar_maquinas
def test_contar_maquinas():
    maquinas_info = [
        ('Machine1', 'hard', 'author1'),
        ('Machine2', 'medium', 'author2')
    ]
    assert contar_maquinas(maquinas_info) == 2
