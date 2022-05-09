from biosteam.units import BinaryDistillation
from biosteam import Stream, settings

settings.set_thermo(["Water", "Ethanol", "Glycol"], cache=True)
feed = Stream("feed", flow=(11, 89, 45))
bp = feed.bubble_point_at_P()
feed.T = bp.T
D1 = BinaryDistillation(
    "D1",
    ins=feed,
    outs=("distillate", "bottoms_product"),
    LHK=("Ethanol", "Water"),
    y_top=0.99,
    x_bot=0.01,
    k=0.75,
    is_divided=True,
)
D1.simulate()
print(D1.results())
