from validate_docbr import CPF as validador


class CPF:

    def __init__(self, documento):
        # documento = str(documento)

        if self.validar_cpf(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido.")
    
    def validar_cpf(self, cpf):
        # if len(cpf) == 11:
        return validador().validate(cpf)
        # raise ValueError("Quantidade de digitos inválida")

    def formatar(self):
        # return f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}"
        return validador().mask(self.cpf)

    def __str__(self):
        return self.formatar()
