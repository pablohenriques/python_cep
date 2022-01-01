from validate_docbr import CNPJ as validador


class CNPJ:

    def __init__(self, documento):
        documento = str(documento)

        if self.validar_cnpj(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido")

    def validar_cnpj(self, cnpj):
        # if len(cnpj) == 14:
        return validador().validate(cnpj)
        # raise ValueError("Quantidade de digito inválida")
    
    def formatar(self):
        return validador().mask(self.cnpj)

    def __str__(self):
        return self.formatar()