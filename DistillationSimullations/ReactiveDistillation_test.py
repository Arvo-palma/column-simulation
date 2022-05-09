from biosteam import Stream, settings
from biosteam.units import BinaryDistillation

settings.set_thermo(["Water", "Methanol"])

feed = Stream("feed", TAG=85.6, MAG=789.5, DAG=165, Methanol=230, NaOCH3=0.023)
bp = feed.bubble_point_at_P()
feed.T = bp.T


D1 = BinaryDistillation(
    "D1",
    ins=feed,
    outs=("Glycerol", "Biodiesel"),
    LHK=("Methanol", "NaOH"),
    y_top=0.79,
    x_bot=0.001,
    k=0.25,
    is_divided=True,
)
D1.simulate()
print(D1.results())
