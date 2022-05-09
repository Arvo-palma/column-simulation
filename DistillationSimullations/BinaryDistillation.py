from biosteam import Stream, settings
from biosteam.units import BinaryDistillation

settings.set_thermo(["Water", "Ethanol", "Ethylene Glycol"], cache=True)

feed = Stream("feed", flow=(29.6, 215, 0.4))
bp = feed.bubble_point_at_P()
feed.T = bp.T

D1 = BinaryDistillation(
    "D1",
    ins=feed,
    outs=("distillate", "bottoms_product"),
    LHK=("Ethanol", "Water"),
    y_top=0.99,
    x_bot=0.01,
    k=0.8,
    is_divided=True,
)
D1.simulate()
print(D1.results())
