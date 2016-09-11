from pythonds.basic.queue import Queue

def hotPotato(nameList, num):
	simqueue = Queue()

	for name in nameList:
		simqueue.enqueue(name)

	while simqueue.size() > 1:
		for i in range (num):
			simqueue.enqueue(simqueue.dequeue())


		simqueue.dequeue()

	return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))