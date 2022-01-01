import requests

class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.validar_cep(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido")

    def validar_cep(self, cep):
        if len(cep) == 8:
            return True
        return False

    def formatar(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"
    
    def retornar_cep_viacep(self):
        url = 'https://viacep.com.br/ws/{}/json/'.format(self.cep)
        req = requests.get(url)
        dados = req.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )

    def __str__(self):
        return self.formatar()

if __name__ == "__main__":
    #cep = 77777888
    cep = '01001000'
    c = BuscaEndereco(cep)
    print(f"CEP: {c}")
    print(f"{c.retornar_cep_viacep()}")

    # url https://viacep.com.br/ws/01001000/json/