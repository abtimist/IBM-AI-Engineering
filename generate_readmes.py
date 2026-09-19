import os
import glob

# Master dict for courses mapping id -> (Title, About, What I Learned, Skills)
courses_data = {
    1: ("Machine Learning with Python", 
        "This course introduces the core concepts of Machine Learning, covering both supervised and unsupervised learning techniques using Scikit-learn.",
        ["Supervised Learning (Classification and Regression)", "Unsupervised Learning (Clustering and Dimensionality Reduction)", "Model Evaluation and Metrics", "Scikit-learn Pipelines"],
        ["Python", "Scikit-learn", "Classification", "Regression", "Clustering"]),
    2: ("Introduction to Deep Learning & Neural Networks with Keras",
        "This foundational deep learning course introduces neural network architectures and practical implementation using Keras and TensorFlow.",
        ["Neural Network Fundamentals", "Forward and Backward Propagation", "Building models with Keras", "Optimizers and Loss Functions"],
        ["Deep Learning", "Keras", "TensorFlow", "Neural Networks"]),
    3: ("Deep Learning with Keras and Tensorflow",
        "This course dives deeper into Keras and TensorFlow, focusing on Convolutional Neural Networks (CNNs) and deep learning for computer vision.",
        ["Convolutional Neural Networks (CNNs)", "Image Classification", "Data Augmentation", "Transfer Learning"],
        ["Computer Vision", "CNNs", "Transfer Learning"]),
    4: ("Introduction to Neural Networks and PyTorch",
        "This course covers the fundamentals of building deep learning models from scratch using PyTorch.",
        ["Tensors and Autograd in PyTorch", "Linear Regression and Logistic Regression with PyTorch", "Deep Neural Networks", "PyTorch Data Loaders"],
        ["PyTorch", "Autograd", "Neural Networks"]),
    5: ("Deep Learning with PyTorch",
        "This course explores advanced PyTorch techniques, focusing on CNNs, image classification, and transfer learning.",
        ["CNN architectures in PyTorch", "Transfer Learning (ResNet, VGG)", "Image Data Augmentation", "Model evaluation and tuning"],
        ["PyTorch", "Computer Vision", "CNNs", "Transfer Learning"]),
    6: ("AI Capstone Project with Deep Learning",
        "This capstone project focuses on building, training, evaluating, and comparing end-to-end Deep Learning models for satellite land/agricultural image classification.",
        ["End-to-End Deep Learning Pipelines", "Comparative Analysis of PyTorch vs Keras", "Vision Transformers (ViT)", "CNN-ViT Hybrid Architectures"],
        ["Model Evaluation", "Vision Transformers", "Keras", "PyTorch"]),
    7: ("Generative AI and LLMs: Architecture and Data Preparation",
        "This course covers the foundational architecture of Large Language Models (LLMs), tokenization, and data preparation techniques.",
        ["Generative AI Libraries", "LLM Architecture", "Tokenization Techniques", "NLP Data Loading"],
        ["Generative AI", "LLMs", "Tokenization", "NLP"]),
    8: ("Gen AI Foundational Models for NLP & Language Understanding",
        "This course explores foundational NLP models, sequence-to-sequence architectures, and word embeddings.",
        ["Word Embeddings (Word2Vec)", "Sequence-to-Sequence Models", "Feed Forward Neural Networks", "Document Classification"],
        ["NLP", "Word2Vec", "Seq2Seq"]),
    9: ("Generative AI Language Modeling with Transformers",
        "This course dives into the core architecture of Transformers, attention mechanisms, and building language models.",
        ["Transformer Fundamentals", "Self-Attention Mechanism", "Positional Encoding", "Encoder and Decoder Models"],
        ["Transformers", "Attention Mechanism", "Language Modeling"]),
    10: ("Generative AI Engineering and Fine-Tuning Transformers",
         "This course covers generative AI engineering and fine-tuning strategies like LoRA and QLoRA for adapting foundational models.",
         ["Fine-Tuning Strategies", "Parameter-Efficient Fine-Tuning (PEFT)", "LoRA and QLoRA", "Hugging Face Model Hub"],
         ["Fine-Tuning", "LoRA", "Hugging Face"]),
    11: ("Generative AI Advanced Fine-Tuning for LLMs",
         "This course focuses on advanced fine-tuning techniques for LLMs including DPO, Reward Modeling, and PPO.",
         ["Instruction Fine-Tuning", "Reward Modeling", "Proximal Policy Optimization (PPO)", "Direct Preference Optimization (DPO)"],
         ["RLHF", "DPO", "PPO", "Reward Modeling"]),
    12: ("Fundamentals of AI Agents Using RAG and LangChain",
         "This course introduces building AI agents, utilizing LangChain, and implementing Retrieval-Augmented Generation (RAG).",
         ["Retrieval-Augmented Generation (RAG)", "LangChain Framework", "In-Context Learning", "Building AI Agents"],
         ["RAG", "LangChain", "AI Agents"]),
    13: ("Project: Generative AI",
         "This capstone project applies generative AI techniques to build a QA bot leveraging RAG, LangChain, and a Gradio interface.",
         ["Building a QA Bot", "Vector Stores and Embeddings", "Gradio UI Integration", "End-to-end LLM Applications"],
         ["RAG", "LangChain", "Gradio", "Vector Stores"])
}

import re
root_dir = "/home/abhishek/Documents/IBM-AI-Engineering"
# Generate Course READMEs
for i in range(1, 14):
    course_folders = glob.glob(os.path.join(root_dir, f"Course-{i}-*"))
    if not course_folders: continue
    folder = course_folders[0]
    
    title, about, learned, skills = courses_data[i]
    learned_list = "\n".join([f"* {item}" for item in learned])
    skills_list = "\n".join([f"* {item}" for item in skills])
    
    notebooks = sorted(glob.glob(os.path.join(folder, "notebooks", "*.ipynb")))
    notebook_list = "\n".join([f"* [{os.path.basename(n).replace('.ipynb', '').replace('_', ' ')}](./notebooks/{os.path.basename(n)})" for n in notebooks])
    if not notebook_list:
        notebook_list = "* No notebooks found."
        
    resources = sorted(glob.glob(os.path.join(folder, "resources", "*")))
    resource_list = ""
    if resources:
        resource_list = "\n## Resources\n" + "\n".join([f"* [{os.path.basename(r).replace('.pdf', '').replace('_', ' ')}](./resources/{os.path.basename(r)})" for r in resources]) + "\n"

    content = f"""# Course {i} — {title}

## Certificate
<div align="center">
  <a href="./certificate/certificate.pdf">
    <img src="./certificate/certificate.png" alt="Course {i} Certificate" width="700">
  </a>
</div>

## About the Course
{about}

## What I Learned
{learned_list}

## Project Files / Notebooks
{notebook_list}
{resource_list}
## Skills Demonstrated
{skills_list}
"""
    with open(os.path.join(folder, "README.md"), "w") as f:
        f.write(content)

# Update Root README
root_readme_content = """# IBM AI Engineering Professional Certificate Portfolio

This repository documents my completion of the **[IBM AI Engineering Professional Certificate](https://www.coursera.org/professional-certificates/ai-engineer)** on Coursera. It contains all course certificates, learning summaries, and the extensive projects completed throughout the program, including the final Capstone projects.

## Professional Certificate

<div align="center">
  <table style="border: none; background-color: transparent;">
    <tr style="border: none; background-color: transparent;">
      <td align="center" style="border: none; background-color: transparent;">
        <a href="./certificate/certificate.pdf">
          <img src="./certificate/certificate.png" alt="IBM AI Engineering Professional Certificate" width="600">
        </a>
      </td>
      <td align="center" style="border: none; background-color: transparent;">
        <a href="https://www.coursera.org/professional-certificates/ai-engineer"><b>View Program on Coursera</b></a>
      </td>
    </tr>
  </table>
</div>

## Courses

The program consists of 13 distinct courses. Click on each course to view the specific certificate, learning objectives, and related project work.

| Course | Topics / Skills | Project |
| :--- | :--- | :--- |
| [Course 1: Machine Learning with Python](./Course-1-Machine-Learning-with-Python) | Scikit-learn, Classification, Regression | ML Pipeline Implementation |
| [Course 2: Introduction to Deep Learning & Neural Networks with Keras](./Course-2-Introduction-to-Deep-Learning) | Neural Networks, Keras, TensorFlow | Simple Neural Net Implementation |
| [Course 3: Deep Learning with Keras and Tensorflow](./Course-3-Deep-Learning-Keras-TensorFlow) | CNNs, Computer Vision, Transfer Learning | CNN Image Classifier |
| [Course 4: Introduction to Neural Networks and PyTorch](./Course-4-Neural-Networks-PyTorch) | PyTorch, Tensors, Autograd | PyTorch Logistic Regression |
| [Course 5: Deep Learning with PyTorch](./Course-5-Deep-Learning-PyTorch) | PyTorch, Transfer Learning (ResNet, VGG) | PyTorch Image Classifier |
| [Course 6: AI Capstone Project with Deep Learning](./Course-6-AI-Capstone-Deep-Learning) | ViT, Keras vs PyTorch, Model Evaluation | **Satellite Image Classification Capstone** |
| [Course 7: Generative AI and LLMs: Architecture and Data Preparation](./Course-7-Generative-AI-LLMs-Architecture) | LLM Architecture, Tokenization, Data Loaders | NLP Tokenization Pipeline |
| [Course 8: Gen AI Foundational Models for NLP & Language Understanding](./Course-8-Gen-AI-NLP-Language-Understanding) | Word2Vec, Seq2Seq, Document Classification | Text Classification Model |
| [Course 9: Generative AI Language Modeling with Transformers](./Course-9-Generative-AI-Language-Modeling) | Attention Mechanism, Positional Encoding | Transformer Model Walkthrough |
| [Course 10: Generative AI Engineering and Fine-Tuning Transformers](./Course-10-Generative-AI-Engineering-FineTuning) | LoRA, QLoRA, PEFT, Hugging Face | LLM Fine-Tuning Implementation |
| [Course 11: Generative AI Advanced Fine-Tuning for LLMs](./Course-11-Generative-AI-Advanced-FineTuning) | RLHF, DPO, PPO, Reward Modeling | Advanced RLHF Pipeline |
| [Course 12: Fundamentals of AI Agents Using RAG and LangChain](./Course-12-AI-Agents-RAG-LangChain) | RAG, LangChain, AI Agents | Simple LangChain Agent |
| [Course 13: Project: Generative AI](./Course-13-Project-Generative-AI) | RAG, Vector Stores, Gradio UI | **Generative AI QA Bot Capstone** |

## Skills & Tools

Throughout the program, I developed proficiency in the following tools and techniques:

* **Programming:** Python, Jupyter Notebook
* **Libraries:** Scikit-learn, Pandas, NumPy, Matplotlib, Hugging Face
* **Deep Learning Frameworks:** Keras, TensorFlow, PyTorch
* **Machine Learning:** Regression, Classification, Clustering, Ensembles
* **Computer Vision:** Convolutional Neural Networks (CNNs), Vision Transformers (ViT), Transfer Learning
* **Natural Language Processing:** Word2Vec, Seq2Seq, Transformers, Attention Mechanisms
* **Generative AI:** Large Language Models (LLMs), PEFT (LoRA, QLoRA), RLHF (DPO, PPO), LangChain, RAG

## Projects

The primary practical components of this program were the extensive capstone projects bridging together the concepts learned across multiple courses.

* **[AI Capstone Project with Deep Learning (Course 6)](./Course-6-AI-Capstone-Deep-Learning)**: Developed an end-to-end deep learning pipeline for satellite image classification. Designed and compared multiple architectures including standard CNNs, Vision Transformers (ViTs), and hybrid models using both Keras and PyTorch.
* **[Project: Generative AI (Course 13)](./Course-13-Project-Generative-AI)**: Constructed a robust Retrieval-Augmented Generation (RAG) Question & Answering bot using LangChain. Implemented document chunking, embedded text with vector stores, and deployed an interactive Gradio user interface for the AI agent.

---
**Note:** The project materials within this repository have been reconstructed from publicly available reference materials to serve as a portfolio demonstrating my skills and completion of the IBM AI Engineering curriculum.
"""
with open(os.path.join(root_dir, "README.md"), "w") as f:
    f.write(root_readme_content)

print("All READMEs updated successfully.")
