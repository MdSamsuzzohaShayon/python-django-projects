# ampqurl = "amqps://nhbxceyv:zBLHkN4Nam_5HVxuTJb0Sx8oNi8oSWlE@chimpanzee.rmq.cloudamqp.com/nhbxceyv"
import pika

# parameters = (pika.ConnectionParameters(host='amqps://nhbxceyv:zBLHkN4Nam_5HVxuTJb0Sx8oNi8oSWlE@chimpanzee.rmqcloudamqp.com/nhbxceyv'),)
params = pika.URLParameters("amqps://nhbxceyv:zBLHkN4Nam_5HVxuTJb0Sx8oNi8oSWlE@chimpanzee.rmqcloudamqp.com/nhbxceyv")
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='hello admin')


