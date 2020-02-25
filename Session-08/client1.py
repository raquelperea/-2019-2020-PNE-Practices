import socket

IP = "212.128.253.128"
PORT = 8080

# We create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establishing connection with the server
s.connect((IP, PORT))

#send data to the server
s.send(str.encode("HOLA"))

#Receive data from the server
msg = s.recv(2000)

print("Message from the server: \n")
print(msg.decode("utf-8"))

# Closing the connection
s.close()
