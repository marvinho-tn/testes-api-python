import pika
from consumers.advices_consumer import handle_advice
from shared.core.config import settings

# Função principal para iniciar o consumidor de conselhos
def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(settings.rabbitmq_host))
    channel = connection.channel()

    channel.exchange_declare(exchange="advices", exchange_type="topic")
    result = channel.queue_declare(queue="", exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange="advices", queue=queue_name, routing_key="advice.new")

    print("[*] Worker listening for advices...")

    channel.basic_consume(queue=queue_name, on_message_callback=handle_advice, auto_ack=True)
    channel.start_consuming()

if __name__ == "__main__":
    main()
