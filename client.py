import zmq
import sys


port = 5556
context = zmq.Context()
print "Connecting to server..."
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:%s" % port)
raw_input("Press any key to roll the dice..")
socket.send ("Hello")
message = int(socket.recv())
print "The dice yielded the number ", message
flag=1
while message%6==0 and flag<3:
	print "You get another go"
	raw_input("Press any key to roll the dice..")
	flag+=1
	socket.send("Hello")
	tempmessage=int(socket.recv())
	print "The dice yielded the number ", tempmessage
	message+=tempmessage
	if message%6!=0:
		break
if flag==3:
	print "You got 6 three times"
	print "You can't move, stay where you are.."
else:
	print "You move by ", message," steps"
