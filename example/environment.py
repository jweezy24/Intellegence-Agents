import socket
import random
import json

class environment:
    #initalizes communication
    def __init__(self,ports):
        #initalizes udp listener socket
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #initalizes udp sender
        self.sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #making the socket a broadcast socket so that we don't need to know the ip of agent
        self.sender.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sender.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        #gives socket a port and an ip address to bind to
        self.listener.bind('', 0)
        self.ports = ports

    def make_numbers(self):
        num1 = random.randint(0,10)
        num2 = random.randint(0,10)
        #creating json dictionary to be sent later
        json_dict = {"num1":num1, "num2":num2}
        json_message = json.dumps(json_dict)
        #if there is only one port just send it there
        if type(self.ports) != type([]):
            self.sender.sendto(json_message.encode(), (localhost, self.ports))
        else:
            #if multiple ports exist send it there
            for i in self.ports:
                self.sender.sendto(json_message.encode(), (localhost, i))
