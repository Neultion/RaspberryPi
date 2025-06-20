import socket
#Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('10.1.3.47', 8080)
message = b"This is our message. It will be sent all at once"

try:
    #send data
    print('sending {!r}'.format(message))
    sent = sock.sendto(message,server_address)

    #receive response
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data))
finally:
    print('closing socket')