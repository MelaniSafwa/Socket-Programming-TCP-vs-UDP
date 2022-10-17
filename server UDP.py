import socket

if __name__ == "__main__":
    host = socket.gethostbyname(socket.gethostname())
    port = 4455

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))

    print(f"Server is listening on {host}")

    while True:
        data, addr = server.recvfrom(1024)
        data = data.decode("utf-8")

        print(f"Client : {data}")

        data = data.upper()
        data = data.encode("utf-8")
        server.sendto(data, addr)
        
