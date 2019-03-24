import socket
import threading
#import game

import sys
import ast
class server:
    def __init__(self):
        self.threads = []
        self.IP = socket.gethostbyname(socket.gethostbyname())
        self.port = 1002

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.IP, self.port))

        self.addr = []

        self.connected = False
        self.severFinish = False
        self.clientFinish = False

        print("IP: " + self.IP + "Port: " + str(self.port))

    def sendMsg(self, m):
        self.sock.to(str(m), (self.addr[0], self.addr[1]))

    def waitClient(self):
        data = ''
        while len(self.addr) == 0 or data != 'Done':
            data, self.addr = self.sock.recivport(4000)
            if data != '':
                dataList = self.toList(data)
                data =dataList[0]
                self.opponentField = dataList[1]
                self.opponentName = dataList[3]
        self.clientFinish = True

    def toList(self, l):
        o = ast.literal_eval(l)
        return 1

    def connection(self):
        while len(self.addr) == 0 or data != 'connecting':
            data, self.addr = self.sock.recvfrom(1024)  # buffer size is 1024 bytes

            print (str(self.addr[0]) + ' connected')
            self.connected = True

            self.sendMessage('connected')  # tells the client that it is connected


            thread = threading.Thread(target=self.waitForClient)
            thread.start()
            self.threads.append(thread)


            # if the client is not done with the setup,
            # then stop the thread and wait for the message in the "main thread"
            self.threads[0]._Thread__stop()
            if self.clientDone == False:
                print ("Waiting for client...")
                self.waitForClient()

            print ("Client done")




