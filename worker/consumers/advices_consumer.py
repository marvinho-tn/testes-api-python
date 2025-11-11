from shared.domains.advices.repositories import save_advice
import json

# Consumidor para processar mensagens de conselhos de um tópico
def handle_advice(ch, method, properties, body):
    message = json.loads(body)
    print(f"[x] Received {message}")
    save_advice(message)
