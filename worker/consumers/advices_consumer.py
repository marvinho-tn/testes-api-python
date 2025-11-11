from shared.domains.advices.repositories import save_advice
import json

def handle_advice(ch, method, properties, body):
    message = json.loads(body)
    print(f"[x] Received {message}")
    save_advice(message)
