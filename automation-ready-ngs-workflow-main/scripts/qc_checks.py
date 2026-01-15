import pandas as pd
import os

# automatically find repo root
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

samples = pd.read_csv(os.path.join(repo_root, "data", "sample_metadata.csv"))

# Example QC logic
samples["qc_status"] = "PASS"
samples.loc[samples["sample_id"] == "S3", "qc_status"] = "Low concentration"

# Save results
results_path = os.path.join(repo_root, "results", "qc_results.csv")
samples.to_csv(results_path, index=False)

print(f"QC results saved to {results_path}")
