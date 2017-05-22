#!/usr/bin/env python

import pika

conn = pika.BlockingConnection(pika.ConnectionParameters('192.168.101.89'))

channel = conn.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(
    exchange='',
    routing_key='hello',
    body='hello world'
)

print()