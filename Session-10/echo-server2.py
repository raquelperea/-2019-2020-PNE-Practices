import socket

IP = "127.0.0.1"
PORT = 8082
count = 0

# step 1: Creating a socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Step 2: Bind the socket to the server's IP and PORT
ls.bind((IP, PORT))



# Step 3: Convert into a listening socket
ls.listen()

print("Server is configured! ")

while True:

    try:
        # Step 4:  Wait for client to conect
        (cs, client_ip_port) = ls.accept() # lc.accept devuelve dos variable que estamos clasificando como cs y client_ip_port
    except KeyboardInterrupt:
        print("Server is done!")
        ls.close()
        exit()

    else:
        # Step 5: Receiving information from the client
        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()
        count += 1

        print("CONNECTION", count)
        print(f"Receiving message: {msg} ")
        print("Cient IP and PORT", client_ip_port)

        # Step 6: Send a response message to the client
        response = f"ECHO:{msg}{count} \n  "
        cs.send(response.encode())
        cs.close()