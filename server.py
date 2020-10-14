import socket,time
so= socket.socket()
serverip = "0.0.0.0"
serverport = 2975
so.bind((serverip, serverport))
so.listen(0)  #ANJIR,, NGEGAS
#s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("MENUNGGU, KLIEN....")
while True:
    handlerSocket,addr = so.accept()
    print("MENDAPATKAN KONEKSI.....")
    time.sleep(2)
    print ("terhubung dengan : ",addr)
    while True:
        pesan=input("Anda : ")
        handlerSocket.send(pesan.encode())
        pesan = handlerSocket.recv(1024).decode()
        print ("client : ",pesan)
