from dataclasses import dataclass

@dataclass
class Motorista:
    nome: str
    cpf: int
    telefone: str
    cnh: str

    def validar_cpf(self):
        if len(str(self.cpf)) != 11:
            raise ValueError("CPF inválido")
    def validar_cnh(self):
        if len(str(self.cnh)) != 15:
            raise ValueError("CNH inválida")


