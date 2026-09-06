#!/bin/bash
source .venv/bin/activate
find /home/abhishek/Documents/IBM-AI-Engineering/ -name "*.ipynb" | while read -r nb; do
    echo "Executing $nb..."
    jupyter nbconvert --to notebook --execute --inplace "$nb" --ExecutePreprocessor.timeout=600 || echo "Error executing $nb, skipping..."
done
echo "All notebook executions attempted."
