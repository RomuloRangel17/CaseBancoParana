import requests
import json
from jsonschema import validate

# URL da API
api_url = "https://jsonplaceholder.typicode.com/users"

# Função para validar o JSON schema
def validate_json_schema(response_json, schema):
    try:
        validate(response_json, schema)
        return True
    except Exception as e:
        print(f"Erro na validação do JSON schema: {e}")
        return False

# Teste para o verbo GET
def test_get_request():
    response = requests.get(api_url)
    assert response.status_code == 200, f"Erro no GET request. HTTP code: {response.status_code}"
    
    # Especificação do JSON schema para usuários
    users_schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "id": {"type": "number"},
                "name": {"type": "string"},
                "username": {"type": "string"},
                "email": {"type": "string"},
                "address": {"type": "object"},
                "phone": {"type": "string"},
                "website": {"type": "string"},
                "company": {"type": "object"}
            },
            "required": ["id", "name", "username", "email", "address", "phone", "website", "company"]
        }
    }

    assert validate_json_schema(response.json(), users_schema), "Erro na validação do JSON schema para GET"
    print(f"Teste GET bem-sucedido! Status Code: {response.status_code}")

# Teste para o verbo POST
def test_post_request():
    # Dados de exemplo para o POST
    post_data = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "johndoe@example.com",
        "phone": "1234567890",
        "website": "https://johndoe.com"
    }

    response = requests.post(api_url, json=post_data)
    assert response.status_code == 201, f"Erro no POST request. HTTP code: {response.status_code}"

    # Especificação do JSON schema para a resposta do POST
    post_response_schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"}
        },
        "required": ["id"]
    }

    assert validate_json_schema(response.json(), post_response_schema), "Erro na validação do JSON schema para POST"
    print(f"Teste POST bem-sucedido! Status Code: {response.status_code}")

    # Você pode adicionar mais validações conforme necessário

# Teste para o verbo PUT
def test_put_request():
    # Supondo que você tenha obtido um ID válido de um usuário existente
    user_id = 1

    # Dados de exemplo para o PUT
    put_data = {
        "name": "Updated Name"
    }

    response = requests.put(f"{api_url}/{user_id}", json=put_data)
    assert response.status_code == 200, f"Erro no PUT request. HTTP code: {response.status_code}"

    # Especificação do JSON schema para a resposta do PUT
    put_response_schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"}
        },
        "required": ["id"]
    }

    assert validate_json_schema(response.json(), put_response_schema), "Erro na validação do JSON schema para PUT"
    print(f"Teste PUT bem-sucedido! Status Code: {response.status_code}")

    # Você pode adicionar mais validações conforme necessário

# Teste para o verbo DELETE
def test_delete_request():
    # Supondo que você tenha obtido um ID válido de um usuário existente
    user_id = 1

    response = requests.delete(f"{api_url}/{user_id}")
    assert response.status_code == 200, f"Erro no DELETE request. HTTP code: {response.status_code}"
    print(f"Teste DELETE bem-sucedido! Status Code: {response.status_code}")

# Execução dos testes
test_get_request()
test_post_request()
test_put_request()
test_delete_request()
