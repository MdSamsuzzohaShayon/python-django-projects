"""
# ampqurl = "amqps://nhbxceyv:zBLHkN4Nam_5HVxuTJb0Sx8oNi8oSWlE@chimpanzee.rmq.cloudamqp.com/nhbxceyv"
import pika

# parameters = (pika.ConnectionParameters(host='amqps://nhbxceyv:zBLHkN4Nam_5HVxuTJb0Sx8oNi8oSWlE@chimpanzee.rmqcloudamqp.com/nhbxceyv'),)
params = pika.URLParameters("amqps://nhbxceyv:zBLHkN4Nam_5HVxuTJb0Sx8oNi8oSWlE@chimpanzee.rmqcloudamqp.com/nhbxceyv")
conn_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue="admin")


def callback(ch, method, properties, body):
    print("received in admin")
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback)

print("Started consuming")
channel.start_consuming()
channel.close()
"""
