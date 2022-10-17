import socket

if __name__ == "__main__":
    host = "192.168.0.106"
    port = 4455
    addr = (host, port)

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    conn = True
    while conn:
        data = input("Enter a message : ")

        if data != "Leave":
            data = data.encode("utf-8")
            client.sendto(data, addr)
            data, addr = client.recvfrom(1024)
            data = data.decode("utf-8")
            print(f"Server: {data}")
        else:
            data = data.encode("utf-8")
            client.sendto(data, addr)
            data, addr = client.recvfrom(1024)
            data = data.decode("utf-8")
            print("[DISCONNECT] Client leave...")
            conn = False
