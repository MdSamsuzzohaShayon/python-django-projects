### RabbitMQ
 - [tutorial](https://www.youtube.com/watch?v=iQ4kENLfaNI&list=PLalrWAGybpB-UHbRDhFsBgXJM1g6T4IvO&index=2)
 - RabbitMQ is a message broker, primary terms are 
   1. Broker -  message broker forwards message to the final destination (Sender does not need to hang around, they can leave the message to broker). Message broker gets a message from producer to consumer through exchange and queue. 
   2. Exchange - An exchange is what a producer always sends it's messages to. There are different types of exchanges. Exchange will push message into one or more queue message will sit in these queues until they are read or consumed by interested party  
   3. Queue - Queues are tied to exchanges in what is known as binding. An exchange can be tied to many queues and queues can be tied to many exchanges.
   4. Producer - (Asynchronous communication) We can have multiple producers pushing messages in to the same message broker. Producer does not have to wait for the message to be delivered.
   5. Consumer - (Asynchronous communication) We can have multiple consumers listening to messages off the message broker. Consumers do not have to wail until messages get sent.
   6. Connection - Every producer or consumer should open a single tcp connection to our rabbit mq broker
   7. Channels - A connection however can have multiple channels.
 - Install RabbitMQ on docker `docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9-management`
 - Access user interface from web __http://localhost:15672/__
 - Now run `python3 consumer.py` and again run this from another terminal `python3 prducer.py`
 - **AMQP** Advanced message queue protocol, (This is not essential for using rabbit )
 - This communication is two way and both the broker and the client can use or pc to run programs or call methods on each other in a similar way to object-oriented languages
 - RabbitMQ uses commands which consist of classes and methods to communicate between clients and the broker
 - for example we might send an exchange declare command that tells the broker want to create a new exchange 
 - In this example exchange is the class and declare is the method
 - **Frame** When a command is sent to or from a rabbitmq broker all the required to execute the command is included in a data structure called a frame
 - 4 frame types by AMQP (every frame start with byte)
   1. Method frame - 
   2. Content header frame 
   3. Body frame
   4. Heartbeat frame
 - Frame type - `1` this is followed by two bytes which is represented the channel that the frame is being sent on
 - Channel - `12` We are sending the frame on channel 12. we have 4 bytes that represent the size of message. Sending the size of the message like this allows us to determine how big the message will be before we have to process it
 - Size - 
 - Frame specific content - Using frame and byte in conjunction with the size allow us to verify the frame specific content
 - Frame end - A byte representing that the frame has ended, The size of the message excludes the frame end byte