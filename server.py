import requests
from pprint import pprint
__print = print
# print = pprint

url = 'http://localhost:8150/schemas'

schema =  {
            "schema_name": "enroll",
            "schema_version": "1.0",
            "attributes": [
                "name",
                "email",
                "document"
            ]
        }

response = requests.post(url=url, json=schema)

if response.status_code >= 200 and response.status_code <= 299:
    # sucesso
    print('Status Code', response.status_code)
    print('Reason', response.reason)
    print('Texto', response.text)
    print('JSON', response.json())
else:
    # erros
    print('Status Code', response.status_code)
    print('Reason', response.reason)
    print('Texto', response.text)
