# Função que escolhe aleatoriamente um valor em uma lista:
from secrets import choice

# Função que cria uma lista a partir de uma faixa de valores:
from numpy import arange

# Pacote para manipular arquivos CSV:
import csv

from MethanolDistillation import generate_results

# Gerador de valores de entrada para a simulação do destilador:
def generate_entry(start, stop, step):
    __array = arange(start, stop, step)
    __list = list(__array)
    __one_value = choice(__list)
    return round(__one_value, 1)


# Gerador de linhas completas com entrada e saída de dados da simulação do destilador:
def generate_row():
    methanol_feed = generate_entry(30, 150, 5)
    water_feed = round(methanol_feed * 0.114)
    glycerol_feed = methanol_feed
    k_value = generate_entry(1.1, 7, 0.1)
    temp_value = generate_entry(40, 88, 2)
    P_value = generate_entry(101325, 200000, 1000)
    results = generate_results(
        water_feed,
        methanol_feed,
        glycerol_feed,
        temp_value,
        k_value,
        P_value,
    )
    __row = (
        k_value,
        water_feed,
        methanol_feed,
        glycerol_feed,
        temp_value,
        P_value,
        results[0],
        results[1],
    )
    return __row


# Função que preenche o arquivo com os dados gerados na simulação:
def populate_file(path):
    file = open(path, "w")
    writer = csv.writer(file)
    header = (
        "RR",
        "water_feed(kmol/hr)",
        "methanol_feed(kmol/hr)",
        "glycerol_feed(kmol/hr)",
        "temperature(degC)",
        "pressure(Pa)",
        "utility_cost(USD/hr)",
        "total_purchase_cost(USD)",
    )
    writer.writerow(header)
    value = 0
    # Laço que adiciona linhas de dados ao arquivo na quantidade especificada:
    while value in range(0, 1000):
        writer.writerow(generate_row())
        value += 1

    file.close()


# Chamada da função com o caminho para o arquivo que deve se preenchido:
populate_file("./ins_data.csv")
