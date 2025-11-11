from dataclasses import dataclass

# Modelo de dados para um conselho
@dataclass
class Advice:
    slip: Slip

# Modelo de dados para o conteúdo do conselho
@dataclass
class Slip:
    id: int
    advice: str
