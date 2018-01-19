# -*- coding:utf-8 -*-
import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
count= 0

while True:
    #  Wait for next request from client
    message = socket.recv()
    count+= 1
    print "Received request: ", message, count

    #  Do some 'work'
    time.sleep (1)        #   Do some 'work'

    #  Send reply back to client
    socket.send(" World")
