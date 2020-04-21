import socket
from Seq1 import Seq
import termcolor

IP = "127.0.0.1"
PORT = 8088
gene_list = ["ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA","AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA","CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT","CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA","AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT"]


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
    print("Waiting for clients to connect")

    try:
        # Step 4:  Wait for client to conect
        (cs, client_ip_port) = ls.accept() # lc.accept devuelve dos variable que estamos clasificando como cs y client_ip_port

    except KeyboardInterrupt:
        print("Server is done!")
        ls.close()
        exit()

    else:
        print("A client has connected to the server!")

        # Step 5: Receiving information from the client
        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()
        msg_comp = msg.split(" ")

        if len(msg_comp) >= 2:
            component_1 = msg_comp[0]
            component_2 = msg_comp[1]
        else:
            component_1 = msg

        if component_1 == "PING":
            termcolor.cprint("PING command!", "green")
            print("OK!")
            response = "OK!" + "\n"

        elif component_1 == "GET":
            for i in range(len(gene_list)):
                if i == int(component_2):
                    termcolor.cprint("GET", "green")
                    print(gene_list[i])
                    response = gene_list[i] + "\n"

        elif component_1 == "COMP":
            termcolor.cprint("COMP", "green")
            seq = Seq(component_2)
            print(seq.complement())
            response = seq.complement() + "\n"

        elif component_1 == "REV":
            termcolor.cprint("REV", "green")
            seq = Seq(component_2)
            print(seq.reverse())
            response = seq.reverse() + "\n"

        elif component_1 == "GENE":
            termcolor.cprint("GENE", "green")
            folder = "../Session-04/"
            seq = Seq("")
            seq = str(seq.read_fasta(folder + component_2 + ".txt"))
            print(seq)
            response = seq + "\n"

        elif component_1 == "INFO":
            response = ""
            bases = ["A", "C", "G", "T"]
            termcolor.cprint("INFO", "green")
            seq = Seq(component_2)
            print(f"Sequence: {seq}")
            print(f"Total length:{seq.len()}")
            for i in bases:
                print(f" {i}: {seq.count_base(i)} {round((seq.count_base(i) / seq.len()) * 100, 2)}%")
                response += f" {i}: {seq.count_base(i)} {round((seq.count_base(i) / seq.len()) * 100, 2)}%"

        print(f"Receiving message: {msg} ")

        # Step 6: Send a response message to the client

        cs.send(response.encode())
        cs.close()

