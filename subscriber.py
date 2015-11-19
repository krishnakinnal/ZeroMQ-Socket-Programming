import sys
import zmq
from random import *
port = 5556

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

housiesize=3
housierange=10

print "Collecting updates from housie publisher..."
socket.connect ("tcp://localhost:%s" % port)
l=[]

for i in range(housiesize):
	l.append(randint(1,housierange))
print "Your set of housie numbers is - ", l

topicfilter = "0"
socket.setsockopt(zmq.SUBSCRIBE, topicfilter)
count=0
stepcount=0
total_value = 0
flag=0

while True:
	count=0
	string = socket.recv()
	topic, messagedata = string.split()
	messagedata=int(messagedata)
	for i in range (housiesize):
		if l[i]==messagedata:
			l[i]=0
	stepcount+=1
	print "Subscribed number is ", messagedata
	for i in range(housiesize):
		if l[i]==0:
			count+=1
	if count==housiesize:
		flag=1
		break

if flag==0:
	print "The publisher has run out of numbers. Game Over"
else:
	print "You have finished the game, after ", stepcount, "steps!"