import http.server
import socketserver
import termcolor
from pathlib import Path

# Define the Server's port
PORT = 8081


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        req_line = self.requestline.split(" ")
        echo_str = req_line[1]
        echo_str = echo_str.split("?")
        echo_line = echo_str[0]


        contents = Path('Error.html').read_text()
        self.send_response(404)

        if echo_line == "/":
            contents = Path('form-EX02.html').read_text()
            self.send_response(200)

        elif echo_line == "/myserver":
            msg_str = echo_str[1]
            msg_str = msg_str.split("=")
            client_msg = msg_str[1]
            input_str = client_msg.split("&")
            input_str = input_str[0]
            if msg_str[-1] == "on":
                contents = Path('form-EX01.html').read_text()
                contents += f"<p>{input_str.upper()}</p>"
            else:
                contents = Path('form-EX01.html').read_text()
                contents += f"<p>{input_str}</p>"


            self.send_response(200)


        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()