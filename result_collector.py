import time
import zmq
import pprint

def result_collector():
	context=zmq.Context()
	results_receiver = context.socket(zmq.PULL)
	results_receiver.bind("tcp://127.0.0.1:5558")
	tot_sum=0
	print "Dice numbers received for each player are:-"
	while True:
		data = results_receiver.recv()
		length=len(data)
		for i in range(length):
			if data[i]==',':
				break
		consumer_id=data[:i]
		dicenumber = data[i+1:]
		print "Consumer = ", consumer_id, "Dicenumber = ", dicenumber
	
result_collector()