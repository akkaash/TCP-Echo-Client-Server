import socket
import sys

print len(sys.argv)

if len(sys.argv) < 3:
    print 'Usage: client.py <ip-address> <port>'
    sys.exit(-1)
else:
    remoteHost = sys.argv[1]
    remotePort = int(sys.argv[2])
    size = 1024

    #create a socket
    mSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #connect to remote host and port
    mSocket.connect((remoteHost, remotePort))

    print "connected to ", mSocket.getsockname()

    #send request to host
    msg = raw_input("Enter message: ")
    mSocket.send(msg)

    #get response
    print "server response: "
    receivedData = mSocket.recv(1024)
    print(receivedData)

    mSocket.close()