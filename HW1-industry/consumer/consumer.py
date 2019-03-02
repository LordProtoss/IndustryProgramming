#!/usr/bin/env python
import pika
import time
import sys

time.sleep(30)
connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbit"))

channel = connection.channel()


channel.queue_declare(queue="hello")

def callback(ch, method, properties, body):
    print("Received:", body, file = sys.stderr)
    

channel.basic_consume(callback,
                      queue="hello",
                      no_ack=True)

print("Waiting for messages", file = sys.stderr)
channel.start_consuming()
