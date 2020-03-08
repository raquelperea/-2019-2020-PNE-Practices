# innit function

class Client:
    def __init__(self, IP, PORT):
        IP = self.IP
        PORT = self.PORT

    def ping(self):
        print("Ok")
        return self

IP = "212"
PORT = 8080
c = Client(IP, PORT)

print(c.ping)