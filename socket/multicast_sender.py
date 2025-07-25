import socket
import struct

message = b'very important data'
multicsat_group = ('224.10.10.10',10000)

#Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Set a timeout so the socket does not block
#indefinitely when trying to recieve data
sock.settimeout(0.2)

#Set the time-to-live for messages to 1 so they do not
#go past the local network segment
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:
    #Send datato the multicast group
    print('sending {!r}'.format(message))
    sent = sock.sendto(message,multicsat_group)

    #Look for responses from all recipients
    while True:
        print('waiting to receive')
        try:
            data, server = sock.recvfromr(16)
        except socket.timeout:
            print('time out, no more responses')
            break
        else:
            print('received {!r} from {}'.format(data,server))
finally:
    print('closing socket')
    sock.close()