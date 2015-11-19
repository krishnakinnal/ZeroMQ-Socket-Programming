import zmq
import random
import sys
import time

port = 5556
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)
housierange=10
numbers=[]
for i in range(housierange):
	numbers.append(i+1)
random.shuffle(numbers)
numbers.append(numbers[0])
for i in range(housierange+1):
	topic = 0
	if i!=0:
		print "Published number - %d" % (numbers[i])
	socket.send("%d %d" % (topic, numbers[i]))
	time.sleep(1)