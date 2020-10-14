import socket
handlerSocket = socket.socket()
serverip = "127.0.0.1"
port = 2975
handlerSocket.connect((serverip, port))
print ("KONEKSI KE SERVER BERHASIL")
while True:
    pesan=handlerSocket.recv(1024).decode()
    print ("server :",pesan)
    pesan = input("PESAN ANDA> ")
    handlerSocket.send(pesan.encode())
