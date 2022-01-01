from cnpj import CNPJ
from cpf import CPF


class Documento:

    @staticmethod
    def criar_documento(documento):
        if len(documento) == 11:
            return CPF(documento)
        elif len(documento) == 14:
            return CNPJ(documento)
        else:
            raise ValueError("Quantidade de dígitos incorreta.")
