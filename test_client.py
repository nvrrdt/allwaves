import socket
import sys
from concurrent.futures import ProcessPoolExecutor
import multiprocessing as mp

def work(i):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (sys.argv[i+1], 10000 + i)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)

    try:

        # Send data
        message = b'This is the message.  It will be repeated.'
        print('sending {!r}'.format(message))
        sock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print('received {!r}'.format(data))

    finally:
        print('closing socket')
        sock.close()

def main():
    ctx = mp.get_context("spawn")
    with ProcessPoolExecutor(mp_context=ctx) as pool:
        for i in range(4):
            pool.submit(work, i)

if __name__ == "__main__":
    main()