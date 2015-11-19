import zmq
import time
import sys
import random


port=5556
context=zmq.Context()
socket=context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)
while 1:
	message=socket.recv()
	number=random.randint(1,6)
	print "Random Number is : ", number
	socket.send("%d" % number)