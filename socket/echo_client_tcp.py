import socket

#Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect the socket to the port where the server is listening
server_address = ('10.1.3.47',999)
print('connecting to {} port {}'.format(*server_address))
try:
    #send data
    message = b'It is very long massage but will only be transmitted in chunks of 16 at a time'
    print('sending {!r}'.format(message))
    socket.sendall(message)

    #Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))
finally:
    print('closing socket')
