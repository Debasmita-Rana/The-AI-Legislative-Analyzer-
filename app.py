import sys
import os

# Add src folder to path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from pipeline import citizen_dashboard_pipeline

# Read policy file
with open("data/policy.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Run pipeline
output = citizen_dashboard_pipeline(text)

# Print clean output
print("\nCitizen Friendly Summary:\n")
print(output)