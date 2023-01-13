import pika


def on_message_recieved(ch, method, properties, body):
    print(f"received new message: {body}")


conn_params = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(conn_params)

channel = connection.channel()

# Declate same queue in the consumer and the producer. Does not matter the queue is declared twice, RabbitMQ will declare it only once.
channel.queue_declare(queue="letterbox")

channel.basic_consume(queue='letterbox', auto_ack=True, on_message_callback=on_message_recieved)

print("Start consuming")

channel.start_consuming()
