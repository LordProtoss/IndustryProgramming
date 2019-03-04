#!/usr/bin/env python
import pika
import time
import numpy as np
import sys

time.sleep(30)
connection = pika.BlockingConnection(pika.ConnectionParameters("rabbit"))

channel = connection.channel()
channel.queue_declare(queue="hello")
while True:
    gen = np.random.rand()
    t = 1 + np.random.rand()
    channel.basic_publish(exchange="",
        	          routing_key="hello",
        	          body=str(gen))
    print("Sent:", gen, file = sys.stderr)
    time.sleep(t)

connection.close()
