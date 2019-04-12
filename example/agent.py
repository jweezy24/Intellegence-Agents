import socket
import matplotlib.pyplot as plt
import json

class agent:
    def __init__(self,port):
        #initalizes udp listener socket
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #initalizes udp sender
        self.sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #gives socket a port and an ip address to bind to
        #we assign a port so that the environment knows where
        #to send the packet
        self.listener.bind('', port)

    #method to listen for packets
    def listen(self):
        #listens for packet
        message, address = self.listener.recvfrom(1024)
        #after recieving packet translates it
        self.translate(message,address)

    #translates the packet to be put on a graph
    def translate(self,message,address):
        #we are sending json packets.
        #to grab the data in the packets we use the python json library to read
        #the information
        points = json.loads(message)['points']
        #we are now plotting the line on a grid
        plt.plot(points[0], points[1], 'ro')
        #show the graph for user
        plt.show()
        #sends a success message to the environment
        #this will tell the environment know we are ready for the next line to make
        self.sender.sendto("success", address)
