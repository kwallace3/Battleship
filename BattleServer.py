#!/usr/bin/env
# Server for multithreaded chat application
# Usage: Open terminal/cmd and run "python ChatServer.py"
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

# Set up chat server
# Store client sockets
import self as self

class setUpConn():
    
clients = {}

HOST = ''
PORT = input('Enter server port: ')
if not PORT:
    PORT = 2000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

# Create a TCP server socket
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)


# Handles incomming connections
def accept_incoming_connections():
    while True:
        # Set up a new connection from the chat client
        client, client_address = SERVER.accept()
        # print("%s:%s has connected." % client_address)
        # Send greeting message
        client.send("Welcome to Battleship! Please type your name and press enter...".encode("utf8"))
        # Start client thread to handle the new connection
        Thread(target=handle_client, args=(client,)).start()


# Handles a single client connection, taking client socket as argument
def handle_client(client):
    # Get name from chat client
    name = client.recv(BUFSIZ).decode("utf8")
    # Send welcome message to chat client
    # Broadcast to all other connected chat clients about new client joining the chat room

    # Add new pair client socket, name to the clients pool
    clients[client] = name


    while True:
        # Receive message from client
        #msg = client.recv(BUFSIZ)
        msg = self.takeTurn(client.recv(BUFSIZ))
        # If it is not a {quit} message from client, then broadcast the
        # message to the rest of the connected chat clients
        # Else server acks the {quit} message, deletes the client from
        # the chat pool, and informs everyone
        if msg != "{quit}".encode("utf8"):
            broadcast(msg, name + ": ")
        else:
            client.send("{quit}".encode("utf8"))
            client.close()
            del clients[client]

            broadcast(msg.encode("utf8"))
            break


# Broadcasts a message to all the clients, using prefix for name identification
def broadcast(msg, prefix=""):
    for sock in clients:
        sock.send(prefix.encode("utf8") + msg)


def main():
    # Start listening to client connections
    SERVER.listen(2)
    print("Waiting for connection...")
    # Start the accepting connections thread
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    # Wait for the accepting connections thread to stop
    ACCEPT_THREAD.join()

    # Close the server socket
    SERVER.close()


if __name__ == "__main__":
    main()
