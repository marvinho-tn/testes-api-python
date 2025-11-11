from shared.domains.advices.repositories import get_count_advices
from shared.domains.advices.schemas import AdviceCountRead

class AdviceService:
    def get_advice_count(self) -> int:
        count = get_count_advices()
        return AdviceCountRead(count=count)