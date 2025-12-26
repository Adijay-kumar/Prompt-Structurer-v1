# Prompt Structure-Based Rewriter (Local LLM)
## Overview

Prompt Structure-Based Rewriter is a *local LLM-powered system* that transforms vague, incomplete, or low-quality user prompts into clear, structured, and high-performing prompts optimized for Large Language Models.

Unlike template-driven or rule-based approaches, this project leverages a locally running Large Language Model to reason about user intent, infer missing context, and reconstruct prompts with professional clarity and structure.

The system is designed primarily for learning, experimentation, and offline AI tooling, with a strong emphasis on understanding why prompt engineering is a semantic reasoning problem.

## Motivation

Many users experience poor results from LLMs not due to model limitations, but due to poorly formulated prompts.

### Common problems include:

- Ambiguous or underspecified instructions

- Missing role, audience, or domain context

- Lack of constraints or success criteria

- Unclear or inconsistent output expectations

>This project exists to address these issues by acting as an intelligent prompt refiner, demonstrating how LLMs can be used to improve human–AI interaction quality.

## Why a Large Language Model Is Required

Prompt enhancement is fundamentally a semantic reasoning task, not a formatting task.

### A Large Language Model is required to:

- Interpret vague or incomplete user intent

- Infer missing roles, constraints, and context

- Reconstruct instructions in a structured and coherent manner

- Generalize across domains without hardcoded logic

### Rule-based systems, regex, or static templates fail because they lack:

- Contextual understanding

- Intent inference

- Language-level abstraction

- Prompt refinement requires reasoning, not rules.
Therefore, a Large Language Model is a necessity—not an implementation choice.

## Why Local Execution (No External APIs)

This project intentionally avoids third-party APIs and cloud-based inference.

*Key reasons*:

- Fully offline execution

- No usage costs or rate limits

- No dependency on external vendors

- Greater transparency into model behavior

- Better suitability for learning, experimentation, and system-level understanding

- Complete ownership of the inference pipeline

- This design choice prioritizes control, privacy, and educational value over convenience.

# Tech Stack


### Core
- Python

### Backend
- FastAPI
- Uvicorn

### Frontend
- Streamlit

### LLM & NLP
- Ollama
- scikit-learn (TF-IDF, cosine similarity)

### Utilities
- Hugging Face Datasets
- Requests

### Tooling
- Git & GitHub

#  Work-Flow
```

User Input
   ↓
Embedding Generation
   ↓
Semantic Search
   ↓
Intent Analysis
   ↓
LLM Processing
   ├─ Role Selection
   ├─ Task Enhancement
   ├─ Instruction Refinement
   └─ Output Structuring
   ↓
Final Enhanced Prompt


``` 
 
## Installation & Setup

### 1. Clone the repository

> **Note:** Make sure Git is installed on your system. You can download it from [https://git-scm.com/downloads](https://git-scm.com/downloads)


```bash
git clone https://github.com/Adijay-kumar/Prompt-Structurer-v1.git
cd Prompt-Structurer-v1
```
### 2. Create a virtual environment

#### It's recommended to use venv to avoid conflicts:

```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### Windows
```bash
.\venv\Scripts\activate
```

#### Mac/Linux
```bash
source venv/bin/activate
```
### 4. Install dependencies
```bash
pip install -r requirements.txt
```
### 5. Run the backend with Uvicorn

```bash
uvicorn backend:main --reload
```
### 6. Run the Streamlit frontend

```bash
streamlit run app.py
```

## Limitations

- Output quality depends on the chosen local LLM and its capabilities

- Requires adequate system resources (CPU/RAM, optional GPU)

- Not designed for high-throughput or production-scale workloads

- Does not include built-in content moderation or safety filtering


> This project is intended for educational and experimental use.
Responsible usage is expected when working with generative models.

## Future Improvements

- Multiple enhancement styles (concise, detailed, creative)

- Adjustable output verbosity

- Prompt quality scoring or feedback

- Easier model swapping and configuration

- Prompt history, export, and versioning

- Structured pipelines for safer and more controlled execution

## Educational Value

This project serves as both a practical tool and a learning artifact.

### It helps learners understand:

- Core principles of prompt engineering

- Why semantic tasks require LLMs over rule-based systems

- How intent, context, and constraints influence LLM outputs

- How to run and reason about LLMs locally without external APIs

> Non-Goals

- This project is not a prompt marketplace

- It is not a production-ready SaaS tool

- It does not aim to replace human judgment in prompt design

#### The primary objective is understanding, experimentation, and skill development.
