# 📘 Prompt Engineering (2025) — Summary from Lee Boonstra's Official Guide

> “You don’t need to be a data scientist or machine learning engineer – everyone can write a prompt.”

---

## 1. What Is Prompt Engineering?

Prompt Engineering is the process of designing high-quality prompts that guide LLMs (like Gemini, GPT, Claude) to produce better output.

LLMs are just next-token predictors — they take your input and try to guess the next most likely word/token based on training data.

### 📌 Why it matters:
- A poor prompt gives confusing or wrong output  
- A good prompt gives useful, accurate, and creative answers  
- It’s not just about *what* you ask, but *how* you ask  

---

## ⚙ 2. LLM Output Configuration

LLMs have configurable settings that change how they respond:

### 🔹 Output Length
- Controls how long the answer will be.
- Shorter responses = less cost, faster
- Longer responses = more detailed, but heavier on performance
- Doesn’t affect style — just trims the response when limit is reached

### 🔹 Temperature
> “Controls the degree of randomness.”

- `0` → very deterministic (same answer every time)  
- `1.0` → more creative, diverse responses  
- Think of it like a “creativity level”

### 🔹 Top-K & Top-P (Nucleus Sampling)
- **Top-K** = choose from top K likely next words (e.g., K=1 = only most likely one)
- **Top-P** = choose from top words until the total probability reaches P (e.g., 0.95 = 95%)

You can combine `Top-K`, `Top-P`, and `Temperature` to balance creativity and control.

### ✅ Recommended starting values:
| Purpose       | Temperature | Top-P | Top-K |
|---------------|-------------|-------|-------|
| Balanced      | 0.2         | 0.95  | 30    |
| Creative      | 0.9         | 0.99  | 40    |
| Factual/Math  | 0.0         | —     | —     |

---

## 🎯 3. Prompting Techniques

### 🔹 Zero-Shot Prompting
Ask a direct question with **no examples**.  
**Example:**  
> “Classify this review as positive, neutral, or negative.”

### 🔹 One-Shot / Few-Shot Prompting
Provide one or more examples in the prompt to guide the model.  
> Used to teach the model your preferred structure or format.

🧠 Few-shot = more reliable when task is complex.

---

## 🧩 4. System, Role, and Contextual Prompting

### 🔹 System Prompting
> “Defines the model’s fundamental capabilities and structure of output.”  
Instruct the model to respond in a certain format.  
**Example:** “Only reply in JSON.”

### 🔹 Role Prompting
> “Assigns a character or identity to the model.”  
**Example:** “Act as a travel guide.”

### 🔹 Contextual Prompting
> “Provides background or current task context.”  
**Example:** 
- “Context: my main file is using FastAPI as backend.”

---

## ⏪ 5. Step-Back Prompting

> “Ask a general question first, then use that as context to solve the specific task.”

**Example:**
**(System Prompt):**   
> “Ask users to tell two numbers and then give them sum of those numbers.”  
**(Chat Flow):**  
> Bot: “Tell me two numbers.”  
> User: “2 and 4”  
> Bot: “sum = 6”

🔍 Purpose: Activate background knowledge before giving the answer.

---

## 🔗 6. Chain of Thought (CoT)

> “Let’s think step by step.”

Encourages the model to explain its reasoning before giving the final answer.

### 💡 Useful for:
- Math problems  
- Logic puzzles  
- Code generation  
- Planning tasks  

---

## 🧠 7. Self-Consistency

> “Ask the same question multiple times with slightly different outputs, and choose the most common answer.”

✅ **Benefit**: Improves accuracy by filtering out randomness  
⚠ **Drawback**: More compute and time needed

---

## 🌳 8. Tree of Thoughts (ToT)

> “Think in multiple directions at once.” OR 
> “Aik problem ko solve krne ke multiple approaches”

The model explores **multiple reasoning paths** simultaneously (like a decision tree).  
Great for:
- Complex planning  
- Critical decision-making  

---

## 🤖 9. ReAct (Reason + Act)

> “Model reasons + takes actions using tools.”

ReAct = **Reasoning** in natural language + **Action** via tools/API calls

Useful for:
- Agents  
- Tool use  
- Search and retrieval workflows  

---

## ⚡ 10. APE – Automatic Prompt Engineering

> “Write a prompt that writes prompts.”

- 1.Model generates **prompt variations**
- 2.You score them using metrics like BLEU or ROUGE
- 3.Then pick the best performing one

---

## 💻 11. Code Prompting

### ✨ Types:
- **Generate code** (Bash, Python, etc.)
- **Explain code** (step-by-step)
- **Translate code** (e.g., Bash → Python)
- **Debug/Review** (get suggestions or fixes)

---

## 🖼 12. Multimodal Prompting

> “Using images + text + audio in prompts.”

If the model supports it, you can combine images, audio, and text into a single prompt to provide richer context.

---

## 🧠 13. Best Practices for Prompt Engineering

✅ Provide examples — especially for few-shot  
✅ Keep it simple — short and clear wins  
✅ Be specific — tell exactly what format/tone/output you want  
✅ Use variables — like `{city}`, `{topic}` for flexibility  
✅ Use positive instructions over negative constraints  
✅ Document your prompts — log versions, outputs, and styles  

---

## 📌 Final Summary (in plain words)

> “Prompt Engineering is not just about writing a question, it's about **guiding the model step-by-step** using structure, roles, tone, and clear examples. The goal is to get the most accurate, creative, or useful output for your task — and yes, you can do this even if you’re not a developer.”
