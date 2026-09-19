#!/bin/bash
set -e

# Rename spaces to underscores for all files in all courses to make URLs nicer
for d in Course-*; do
  if [ -d "$d" ]; then
    find "$d" -maxdepth 1 -type f -name "* *" | while read -r f; do
      mv "$f" "${f// /_}"
    done
  fi
done

# Course 7 and 8 resources
mkdir -p Course-7-Generative-AI-LLMs-Architecture/resources Course-8-Gen-AI-NLP-Language-Understanding/resources
mv Course-7-Generative-AI-LLMs-Architecture/*.pdf Course-7-Generative-AI-LLMs-Architecture/resources/ 2>/dev/null || true
mv Course-8-Gen-AI-NLP-Language-Understanding/*.pdf Course-8-Gen-AI-NLP-Language-Understanding/resources/ 2>/dev/null || true

# Course 9
mkdir -p Course-9-Generative-AI-Language-Modeling/{certificate,notebooks,resources}
mv Course-9-Generative-AI-Language-Modeling/Generative_AI_Language_Modeling_with_Transformers.pdf Course-9-Generative-AI-Language-Modeling/certificate/certificate.pdf
pdftoppm -png -f 1 -l 1 Course-9-Generative-AI-Language-Modeling/certificate/certificate.pdf > Course-9-Generative-AI-Language-Modeling/certificate/certificate.png
mv Course-9-Generative-AI-Language-Modeling/*.ipynb Course-9-Generative-AI-Language-Modeling/notebooks/
mv Course-9-Generative-AI-Language-Modeling/*.pdf Course-9-Generative-AI-Language-Modeling/resources/ 2>/dev/null || true
mv Course-9-Generative-AI-Language-Modeling/Beginner\'s_Guide_to_Transformer_Model_Fundamentals Course-9-Generative-AI-Language-Modeling/resources/ 2>/dev/null || true

# Course 10
mkdir -p Course-10-Generative-AI-Engineering-FineTuning/{certificate,notebooks,resources}
mv Course-10-Generative-AI-Engineering-FineTuning/Generative_AI_Engineering_and_Fine-Tuning_Transformers.pdf Course-10-Generative-AI-Engineering-FineTuning/certificate/certificate.pdf
pdftoppm -png -f 1 -l 1 Course-10-Generative-AI-Engineering-FineTuning/certificate/certificate.pdf > Course-10-Generative-AI-Engineering-FineTuning/certificate/certificate.png
mv Course-10-Generative-AI-Engineering-FineTuning/*.ipynb Course-10-Generative-AI-Engineering-FineTuning/notebooks/
mv Course-10-Generative-AI-Engineering-FineTuning/*.pdf Course-10-Generative-AI-Engineering-FineTuning/resources/ 2>/dev/null || true

# Course 11
mkdir -p Course-11-Generative-AI-Advanced-FineTuning/{certificate,notebooks,resources}
mv Course-11-Generative-AI-Advanced-FineTuning/Generative_AI_Advanced_Fine-Tuning_for_LLMs.pdf Course-11-Generative-AI-Advanced-FineTuning/certificate/certificate.pdf
pdftoppm -png -f 1 -l 1 Course-11-Generative-AI-Advanced-FineTuning/certificate/certificate.pdf > Course-11-Generative-AI-Advanced-FineTuning/certificate/certificate.png
mv Course-11-Generative-AI-Advanced-FineTuning/*.ipynb Course-11-Generative-AI-Advanced-FineTuning/notebooks/
mv Course-11-Generative-AI-Advanced-FineTuning/*.pdf Course-11-Generative-AI-Advanced-FineTuning/resources/ 2>/dev/null || true

# Course 12
# The certificate was mistakenly in Course 13
mkdir -p Course-12-AI-Agents-RAG-LangChain/{certificate,notebooks,resources}
mv Course-13-Project-Generative-AI/Fundamentals_of_AI_Agents_Using_RAG_and_LangChain.pdf Course-12-AI-Agents-RAG-LangChain/certificate/certificate.pdf
pdftoppm -png -f 1 -l 1 Course-12-AI-Agents-RAG-LangChain/certificate/certificate.pdf > Course-12-AI-Agents-RAG-LangChain/certificate/certificate.png
mv Course-12-AI-Agents-RAG-LangChain/*.ipynb Course-12-AI-Agents-RAG-LangChain/notebooks/
mv Course-12-AI-Agents-RAG-LangChain/*.pdf Course-12-AI-Agents-RAG-LangChain/resources/ 2>/dev/null || true

# Course 13
mkdir -p Course-13-Project-Generative-AI/{certificate,notebooks,resources}
mv Course-13-Project-Generative-AI/Project:_Generative_AI_Applications_with_RAG_and_LangChain.pdf Course-13-Project-Generative-AI/certificate/certificate.pdf
pdftoppm -png -f 1 -l 1 Course-13-Project-Generative-AI/certificate/certificate.pdf > Course-13-Project-Generative-AI/certificate/certificate.png
mv Course-13-Project-Generative-AI/*.ipynb Course-13-Project-Generative-AI/notebooks/
mv Course-13-Project-Generative-AI/*.pdf Course-13-Project-Generative-AI/resources/ 2>/dev/null || true

# Main Certificate
mkdir -p certificate
mv IBM_AI_Engineering.pdf certificate/certificate.pdf 2>/dev/null || true
pdftoppm -png -f 1 -l 1 certificate/certificate.pdf > certificate/certificate.png 2>/dev/null || true

