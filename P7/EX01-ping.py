import http.client
import json

SERVER = 'rest.ensembl.org'
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Server {SERVER}")
print(f"URL: {URL}")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET",  ENDPOINT + PARAMS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
dict_ping = json.loads(data1)

ping_value = dict_ping["ping"]

if ping_value == 1:
    print("Ping ok!")













