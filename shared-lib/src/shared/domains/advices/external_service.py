from shared.core.config import settings
from shared.domains.advices.models import Advice, Slip
import httpx

class ExternalAdviceService:
    BASE_URL = settings.advice_api_base_url

    @staticmethod
    def get_advice() -> Advice:
        with httpx.Client() as client:
            response = client.get(f"{ExternalAdviceService.BASE_URL}/advice")
            data = response.json()
            return Advice(slip=Slip(
                id=data["slip"]["id"],
                advice=data["slip"]["advice"]
            ))
