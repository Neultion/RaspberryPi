import socket

#Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket to the port
sever_address = ('10.1.3.47',8080)
print('Starting up on {} port {}'.format(*sever_address))
sock.bind(sever_address)

#Listen for incoming connections
sock.listen(1)

while True:
    #Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from ', client_address)

        #Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the clienr')
                connection.sendall(data)
            else:
                print('no data from ',client_address)
                break
    finally:
        #Clean up the connection
        print("Closing current connection")
        connection.close()