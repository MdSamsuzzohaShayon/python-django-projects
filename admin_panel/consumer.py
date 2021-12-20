# SEND EVENTS 
import pika 

params = pika.URLParameters('amqps://tbnqdpjx:la42FUXSK9NBAyeCNGWBMV8_91CQMgwy@puffin.rmq2.cloudamqp.com/tbnqdpjx')
connection = pika.BlockingConnection(params)
channel =connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print("Recieved in admin")
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback)

print('start consume')

channel.start_consuming()
channel.close()