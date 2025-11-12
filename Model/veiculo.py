from dataclasses import dataclass

@dataclass
class Veiculo:
    placa: str
    modelo: str
    ano: int
    id_motorista: int

    def validar_placa(self):
        if len(str(self.placa)) != 8:
            raise ValueError('Placa Inválida')
        
    def validar_ano(self):
        if type(self.ano) != int:
            raise ValueError('Ano Inválido')
        
