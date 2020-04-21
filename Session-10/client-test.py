from Client0 import Client
# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8083
count = 0
c = Client(IP, PORT)

while count < 5:
    # -- Create a client object
    c.debug_talk(f"Message {count}")
    count+=1
