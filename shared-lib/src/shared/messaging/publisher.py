import pika
import json
from shared.core.config import settings

def publish_advice(advice_id: int, advice_text: str):
    # Conexão com RabbitMQ
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=settings.rabbitmq_host)
    )
    channel = connection.channel()

    # Declara um exchange do tipo 'fanout' (broadcast) ou 'topic'
    channel.exchange_declare(exchange="advices", exchange_type="topic")

    # Mensagem
    message = {
        "id": advice_id,
        "advice": advice_text
    }

    # Publica no exchange com uma routing key
    channel.basic_publish(
        exchange="advices",
        routing_key="advice.new",
        body=json.dumps(message)
    )

    print(f"[x] Sent {message}")

    connection.close()