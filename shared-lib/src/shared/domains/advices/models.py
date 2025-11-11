from dataclasses import dataclass

@dataclass
class Advice:
    slip: Slip

@dataclass
class Slip:
    id: int
    advice: str
