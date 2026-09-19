import os
import glob

courses = [
    (9, "Course-9-Generative-AI-Language-Modeling", "Generative AI Language Modeling with Transformers", "Language modeling, transformer fundamentals, attention mechanism, and positional encoding."),
    (10, "Course-10-Generative-AI-Engineering-FineTuning", "Generative AI Engineering and Fine-Tuning Transformers", "Generative AI engineering, fine-tuning transformers, LoRA, and QLoRA."),
    (11, "Course-11-Generative-AI-Advanced-FineTuning", "Generative AI Advanced Fine-Tuning for LLMs", "Advanced fine-tuning, InstructLab, DPO, reward modeling, and PPO."),
    (12, "Course-12-AI-Agents-RAG-LangChain", "Fundamentals of AI Agents Using RAG and LangChain", "RAG applications, LangChain, contextual learning, and building AI agents."),
    (13, "Course-13-Project-Generative-AI", "Project: Generative AI", "Capstone project applying RAG, LangChain, QA bots, and Gradio interfaces.")
]

for num, folder, title, desc in courses:
    readme_path = os.path.join(folder, "README.md")
    
    notebooks = sorted(glob.glob(os.path.join(folder, "notebooks", "*.ipynb")))
    notebook_list = "\n".join([f"- [{os.path.basename(n).replace('.ipynb', '').replace('_', ' ')}](./notebooks/{os.path.basename(n)})" for n in notebooks])
    
    resources = sorted(glob.glob(os.path.join(folder, "resources", "*")))
    resource_list = ""
    if resources:
        resource_list = "\n## Resources\n" + "\n".join([f"- [{os.path.basename(r).replace('.pdf', '').replace('_', ' ')}](./resources/{os.path.basename(r)})" for r in resources]) + "\n"

    content = f"""# Course {num}: {title}

**Status:** ✅ Completed

## Certificate
<a href="./certificate/certificate.pdf">
    <img src="./certificate/certificate.png" width="100%" alt="Course {num} Certificate">
</a>

## Overview
This course has been completed. It covers {desc}

## Completed Notebooks
{notebook_list}
{resource_list}"""

    with open(readme_path, "w") as f:
        f.write(content)

