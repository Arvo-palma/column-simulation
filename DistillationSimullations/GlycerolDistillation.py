from biosteam.units import BinaryDistillation
from biosteam import Stream, settings

settings.set_thermo(["Water", "Methanol", "Glycerol"], cache=True)
feed = Stream("feed", flow=(80, 100, 25))
# bp = feed.bubble_point_at_P()
feed.T = 200
D1 = BinaryDistillation(
    "D1",
    ins=feed,
    outs=("distillate", "bottoms_product"),
    LHK=("Methanol", "Water"),
    y_top=0.99,
    x_bot=0.01,
    k=5,
    is_divided=True,
    P=900000,
)
D1.simulate()
total_purchase_cost = 0
for cost in D1.purchase_costs:
    total_purchase_cost += D1.purchase_costs[cost]
print(D1.utility_cost, total_purchase_cost)
