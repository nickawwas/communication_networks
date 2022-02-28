from os.path import exists
from socket import socket, AF_INET6, SOCK_STREAM 

# Extract File Name from Request
# - Find End of Line of Request Line
# - Extract Request Line from Request
# - Extract File Name from Request Line
def extract_filename(req):
    req_line_eol = req.find("\r\n")
    req_line = req[0:req_line_eol]
    req_file_path = req_line.split(" ")[1]
    return req_file_path[1:]

# Generate Response Based on Requested File
# When Requested File is Found, Respond with 200 OK
# When Requested File Doesn't Exist, Respond with 404 Not Found
def generate_res(req_file):
    if(not exists(req_file)):
        # Define Response with File Not Found, 404
        return "HTTP/1.1 404 Not Found\n"
    else:
        # Read Contents of File
        with open(req_file, 'r') as file:
            file_content = file.read()

        # Define Response Header, Combine Header and Body
        # Header and Body Seperated By an Additional \n
        res_header = "HTTP/1.1 200 OK\nContent-Type: text/html\n"
        return f"{res_header}\n{file_content}"

# Main Function Called in Script
def main():
    # Set Hostname and Port Variables
    HOSTNAME, PORT = "localhost", 12000

    # Initialize Socket using AF_INET6 and SOCK_STREAM to Specify IPv6 and TCP Respectively 
    s = socket(AF_INET6, SOCK_STREAM)

    try:
        # Bind Hostname and Port Number to Socket as localhost:12000
        s.bind((HOSTNAME, PORT))

        # Open TCP Socket, Listening for Connections on localhost:12000
        s.listen()
        print("Server Listening ...\n")

        while True:
            # Accept Client Connection/Browser Request
            connection, address = s.accept()
            print("Server Connected!\n")

            with connection as c: 
                # Receive HTTP Get Request from Client Connection/Browser
                data = c.recv(1024)

                # Deserialize and Print HTTP Request
                req = data.decode('utf-8')
                print("Request Received:")
                print(req)
                
                # Find and Parse Request to Obtain File Name
                req_file = extract_filename(req)
                print("Requesting File: ", req_file)

                # Generate Response Message Based on Existence of File on Server
                res_str = generate_res(req_file)

                # Serialize HTTP Response
                res = res_str.encode("utf-8")

                # Send All Data Back to Client/Browser and Print Response
                c.sendall(res)
                print("Response Sent:")
                print(res_str)
                
                print("\nListening for Other Requests ...\n")

    except KeyboardInterrupt:
        # Close Socket on Keyboard Interrupt
        print("\nClosing Socket on Keyboard Interrupt!")
    
    except Exception as e:
        # Catch Other Exceptions
        print("Error: ", e)

    # Close Socket
    print("Server Socket Closed!\n")


# Script Starting Point
if __name__ == '__main__':
    main()
