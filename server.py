
from socket import AF_INET, socket, SOCK_DGRAM
from threading import Thread

class server:
    def init(self):
        HOST = ''
        PORT = 10000

        ADDR = (HOST, PORT)
        self.threads = []
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = 10000

        self.addr = []  #client ip and port
        SERVER = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
        SERVER.bind(ADDR)

def sendMsg(self, m):
    self.sock.sendto(str(m), (self.addr[0], self.addr[1])) #send msg to client.
def accept_incoming_connections():
    while True:
        # Set up a new connection from the chat client

        client, client_address = SERVER.accept()
        #print("%s:%s has connected." % client_address)
        # Send greeting messagew
        client.send("Welcome to Battleship! Please type your name and press enter...".encode("utf8"))
        # Start client thread to handle the new connection
        Thread(target=handle_client, args=(client,)).start()



