import pandas as pd

TARGET_CONCENTRATION = 10  # ng/µL
FINAL_VOLUME = 20          # µL
OVERAGE_FACTOR = 1.10      # 10% extra

samples = pd.read_csv("../data/sample_metadata.csv")

def calculate_volumes(row):
    c1 = row["concentration_ng_ul"]
    c2 = TARGET_CONCENTRATION
    v2 = FINAL_VOLUME

    if c1 <= 0:
        return pd.Series([None, None])

    v1 = (c2 * v2) / c1
    buffer = v2 - v1

    return pd.Series([round(v1, 2), round(buffer, 2)])

samples[["dna_volume_ul", "buffer_volume_ul"]] = samples.apply(
    calculate_volumes, axis=1
)

# Apply overage
samples["dna_volume_ul"] *= OVERAGE_FACTOR
samples["buffer_volume_ul"] *= OVERAGE_FACTOR

print(samples)

