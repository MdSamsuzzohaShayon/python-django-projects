# amqps://nhbxceyv:zBLHkN4Nam_5HVxuTJb0Sx8oNi8oSWlE@chimpanzee.rmq.cloudamqp.com/nhbxceyv
# ampqurl = "amqps://nhbxceyv:zBLHkN4Nam_5HVxuTJb0Sx8oNi8oSWlE@chimpanzee.rmq.cloudamqp.com/nhbxceyv"
import pika
import os

# parameters = pika.ConnectionParameters(host='amqps://nhbxceyv:zBLHkN4Nam_5HVxuTJb0Sx8oNi8oSWlE@chimpanzee.rmqcloudamqp.com/nhbxceyv')
# params = pika.URLParameters("amqps://nhbxceyv:zBLHkN4Nam_5HVxuTJb0Sx8oNi8oSWlE@chimpanzee.rmqcloudamqp.com/nhbxceyv")
# conn_params = pika.ConnectionParameters('localhost')
conn_params = pika.ConnectionParameters('mrabbitmq_ser')
# conn_params = pika.ConnectionParameters('amqp://guest:guest@mrabbitmq_ser:5672')
# parameters = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@chimpanzee.rmqcloudamqp.com/nhbxceyv')



connection = pika.BlockingConnection(conn_params)
channel = connection.channel()
channel.queue_declare(queue="admin")


def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='hello admin')
    # channel.basic_publish(exchange='', routing_key='letterbox', body=message)


# connection.close()