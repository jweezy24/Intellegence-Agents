import agent
import environment as env
import threading
import time

#creates a daemon thread to send over packets
def create_daemon(ev):
    t = threading.Thread(target=daemon_listener, args=(ev, ))
    t.daemon = True
    t.name = "Watcher"
    t.start()
#sleeping the thread so the main thread can listen for the packet
def daemon_listener(ev):
    time.sleep(1)
    ev.make_numbers()

def main():
    #initalizing environment and agent
    ev = env.environment(8000)
    worker = agent.agent(8000)
    #creates daemon thread first
    create_daemon(ev)
    #then worker waits for information
    worker.listen()
    #after listening, shows what the socket heard
    worker.show()

main()
