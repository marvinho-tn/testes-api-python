from shared.core.config import settings

# Serviço para operações relacionadas a hello world
class HelloService:
    @staticmethod
    def get_greeting() -> str:
        return f"Bem-vindo à {settings.app_name}!"