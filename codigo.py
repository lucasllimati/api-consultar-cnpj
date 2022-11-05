import requests
import json

def consulta_cnpj(cnpj):
  
  # https://receitaws.com.br/
  # https://receitaws.com.br/api
  # https://developers.receitaws.com.br/#/operations/queryCNPJFree

  url = f'https://receitaws.com.br/v1/cnpj/{cnpj}'
  
  querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX", "cnpj":"16990590000123","plugin":"RF"}

  response = requests.request("GET", url, params=querystring)

  resp = json.loads(response.text)

  print(resp['nome'])
  print(resp['logradouro'])

  print(response.text)

consulta_cnpj("33291488000102")