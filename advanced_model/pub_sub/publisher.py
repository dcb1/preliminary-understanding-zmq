'''
This is how the application will work:

1,The publisher knows in advance how many subscribers it expects. This is just a magic number it gets from somewhere.
2,The publisher starts up and waits for all subscribers to connect. This is the node coordination part. Each subscriber subscribes and then tells the publisher it's ready via another socket.
3,When the publisher has all subscribers connected, it starts to publish data.
'''
__author__ = 'eric.sun'
#
#  Synchronized publisher
#
import zmq

#  We wait for 10 subscribers
SUBSCRIBERS_EXPECTED = 1

def main():
    context = zmq.Context()
    
    # Socket to talk to clients
    publisher = context.socket(zmq.PUB)
    # set SNDHWM, so we don't drop messages for slow subscribers
    publisher.sndhwm = 1100000
    publisher.bind('tcp://*:5561')
    
    # Socket to receive signals
    syncservice = context.socket(zmq.REP)
    syncservice.bind('tcp://*:5562')
    
    # Get synchronization from subscribers
    subscribers= 0
    while subscribers< SUBSCRIBERS_EXPECTED:
        # wait for synchronization request
        msg = syncservice.recv()
        # send synchronization reply
        syncservice.send(b'')
        subscribers+= 1
        print("+1 subscriber (%i/%i)" % (subscribers, SUBSCRIBERS_EXPECTED))
    
    # Now broadcast exactly 1M updates followed by END
    for i in range(1000000):
        publisher.send(b'Rhubarb')
    
    publisher.send(b'END')
    
if __name__ == '__main__':
    main()
