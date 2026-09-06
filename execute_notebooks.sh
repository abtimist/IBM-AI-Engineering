#!/bin/bash

# Setup uv environment
uv venv .venv
source .venv/bin/activate
uv pip install jupyter nbconvert ipykernel
uv pip install numpy pandas matplotlib seaborn scikit-learn
uv pip install tensorflow-cpu keras torch torchvision torchaudio transformers pillow

# Find and execute all notebooks
find /home/abhishek/Documents/IBM-AI-Engineering/ -name "*.ipynb" | while read -r nb; do
    echo "Executing $nb..."
    # Execute and ignore errors, overriding the file inplace
    jupyter nbconvert --to notebook --execute --inplace "$nb" --ExecutePreprocessor.timeout=600 || echo "Error executing $nb, skipping..."
done
echo "All notebook executions attempted."
