import pandas as pd
import string

# Generate 96-well plate positions (A1–H12)
rows = list(string.ascii_uppercase[:8])
cols = list(range(1, 13))
wells = [f"{r}{c}" for r in rows for c in cols]

# Load sample metadata
samples = pd.read_csv("../data/sample_metadata.csv")

if len(samples) > len(wells):
    raise ValueError("Too many samples for a single 96-well plate.")

# Assign wells
samples["well"] = wells[:len(samples)]

# Save plate map
samples[["sample_id", "well"]].to_csv(
    "../data/example_plate_map.csv", index=False
)

print("Plate map generated successfully.")

