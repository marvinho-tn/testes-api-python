from shared.core.config import settings

class HelloService:
    @staticmethod
    def get_greeting() -> str:
        return f"Bem-vindo à {settings.api_name}!"