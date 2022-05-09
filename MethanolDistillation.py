# Importação da classe Destilação Binária e variáveis de configuração dela:
from biosteam.units import BinaryDistillation
from biosteam import Stream, settings

# Função que gera os resultados da destilação:
def generate_results(water, methanol, glycerol, temp, k_value, pressure):
    # Define o pacote de propriedades:
    settings.set_thermo(["Water", "Methanol", "Glycerol"], cache=True)

    # Define as propriedades da alimentação:
    feed = Stream("feed", flow=(water, methanol, glycerol))
    feed.T = temp

    # Cria a destilação, simula e retorna seus custos de utilidade e projeto:
    D1 = BinaryDistillation(
        "D1",
        ins=feed,
        outs=("distillate", "bottoms_product"),
        LHK=("Methanol", "Water"),  # Componentes leve e pesado
        y_top=0.99,  # Fração do componente leve no destilado
        x_bot=0.01,  # Fração do componente pesado no produto de fundo
        k=k_value,  # Razão de refluxo sobre o refluxo mínimo
        is_divided=True,  # Se as sessões de retificação e stripping são separadas
        P=pressure,  # Pressão de operação
    )
    D1.simulate()
    # Etapa que realiza a soma dos custos de projeto para retornar o total:
    total_purchase_cost = 0
    for cost in D1.purchase_costs:
        total_purchase_cost += D1.purchase_costs[cost]
    return (D1.utility_cost, total_purchase_cost)
