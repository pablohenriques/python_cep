from datetime import datetime, timedelta


meses = ["", "jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
semana = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]


class Data:

    def __init__(self):
        self.horario_cadastro = datetime.today()

    def get_mes_cadastro(self):
        numero_mes = self.horario_cadastro.month
        print(f"Número do mês: {numero_mes}")
        return meses[numero_mes]

    def get_dia_semana_cadastro(self):
        numero_dia_semana = self.horario_cadastro.weekday()
        print(f"Número da semana: {numero_dia_semana}")
        return semana[numero_dia_semana]

    def formatar_data(self):
        d_formatada = self.horario_cadastro.strftime("%d/%m/%Y %H:%M")
        return d_formatada

    def get_tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.horario_cadastro
        return tempo_cadastro

    def __str__(self):
        return self.formatar_data()



if __name__ == "__main__":
    d = Data()
    #  print(f"{d.get_mes_cadastro()}")
    # print(f"{d.get_dia_semana_cadastro()}")
    # d.get_mes_cadastro()
    # print(d.formatar_data())
    print(d)
    print(f"Tempo de cadastro: {d.get_tempo_cadastro()}")