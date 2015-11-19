import time
import zmq
from random import *

def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind("tcp://127.0.0.1:5557")

    l=[]
    for i in range(100):
        l.append(randint(1,6))
    print "Pushing dice numbers to the players"
    for num in range(2000):
		zmq_socket.send_json(l)
producer()