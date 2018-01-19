# -*- coding:utf-8 -*-
import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = ":Publish message"
    print "Publish Message: ", message
    #  Do some 'work'
    time.sleep (1)        #   Do some 'work'
    #  Send reply back to client
    socket.send(message)
