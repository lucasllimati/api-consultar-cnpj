import http.client

conn = http.client.HTTPSConnection("receitaws.com.br")

headers = { 'Content-Type': "application/json" }

conn.request("GET", "/v1/cnpj/33291488000102", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))