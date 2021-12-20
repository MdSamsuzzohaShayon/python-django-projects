# amqps://tbnqdpjx:la42FUXSK9NBAyeCNGWBMV8_91CQMgwy@puffin.rmq2.cloudamqp.com/tbnqdpjx

# SEND EVENTS 
import pika 

params = pika.URLParameters('amqps://tbnqdpjx:la42FUXSK9NBAyeCNGWBMV8_91CQMgwy@puffin.rmq2.cloudamqp.com/tbnqdpjx')
connection = pika.BlockingConnection(params)
channel =connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='body')
     