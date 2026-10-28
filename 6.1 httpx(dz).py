import httpx

login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post('http://127.0.0.1:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()

print('Login response:', login_response_data)
print('Status Code:', login_response.status_code)

headers = {
    'Authorization': f'Bearer {login_response_data["token"]["accessToken"]}'
}
authorization_response = httpx.get('http://127.0.0.1:8000/api/v1/users/me', headers=headers)
authorization_response_data = authorization_response.json()

print('Authorization response:', authorization_response_data)
print('Status Code:', authorization_response.status_code)
