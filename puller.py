import time
import zmq
import random
import time

def consumer():
    consumer_id = random.randrange(0,100)
    print "You are player number #%s" % (consumer_id)
    context = zmq.Context()
    print "Pulling dice number from pusher.."
	
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://127.0.0.1:5557")
    consumer_sender = context.socket(zmq.PUSH)
    consumer_sender.connect("tcp://127.0.0.1:5558")
	
    result = consumer_receiver.recv_json()
    dicenumber=result[consumer_id]
    print "Number on the dice is ", dicenumber
    #consumer_sender.send_json(result)
    string=str(consumer_id)+","+str(dicenumber)
    consumer_sender.send("%s" % (string))
consumer()