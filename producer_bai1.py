import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='iot_lab_queue', durable=True)

# Nội dung gửi chứa thông tin của bạn
message = "Xin chao tu ung dung Python AMQP - Vũ Đình Ngọc Minh - B23DCCN569"
channel.basic_publish(exchange='', routing_key='iot_lab_queue', body=message)

print(f" [x] Da gui: '{message}'")
connection.close()