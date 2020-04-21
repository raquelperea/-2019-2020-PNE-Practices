from Client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8088
c = Client(IP, PORT)

print("Testing PING...")
c.talk("PING")

print("Testing GET...")
print(c.talk("GET 0"))
print(c.talk("GET 1"))
print(c.talk("GET 2"))
print(c.talk("GET 3"))
print(c.talk("GET 4"))

print("Testing INFO...")
print(c.talk("INFO AAACCCGGTGTGCACAGTAGATCA"))

print("Testing COMP...")
print(c.talk("COMP AAACCCGGTGTGCACAGTAGATCA"))

print("Testing REV...")
print(c.talk("REV AAACCCGGTGTGCACAGTAGATCA"))

print("Testing GENE...")
print(c.talk("GENE U5"))
print(c.talk("GENE ADA"))
print(c.talk("GENE FRAT1"))
print(c.talk("GENE FXN"))
print(c.talk("GENE RNU6_269P"))





