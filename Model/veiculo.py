from dataclasses import dataclass

@dataclass
class Veiculo:
    placa: str
    modelo: str
    ano: int
    id_motorista: int