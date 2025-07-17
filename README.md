# 🥗 Diet Creator App

**Diet Creator App** is a user-friendly desktop application that generates **personalized weekly diet plans** using Google's Gemini AI. It supports **Greek**, **English**, and **German**, and tailors each plan based on the user's gender, age, lifestyle, and dietary preferences.

---

## ✨ Features

### 🧠 AI-Powered Diet Generator
- Analyzes user input (gender, age, goals, allergies, lifestyle, etc.).
- Automatically generates a **Markdown table** with a weekly diet plan.
- Provides healthy, balanced meals with helpful notes and alternatives.
- Includes a disclaimer at the end for health safety.

### 🌐 Multi-Language Support
- Supports **Greek**, **English**, and **German**.
- The AI responds in the selected language, adapting tone and content accordingly.

### ❓ Ask Questions About Your Diet
- After generating your plan, you can **ask follow-up questions** about the diet.
- The AI will answer **only based on the content of your generated plan**.
- Examples:
  - "What do I eat for breakfast on Tuesday?"
  - "Can I swap lunch and dinner?"
  - "Does the plan include dairy?"

---

## ⚙️ How It Works

1. **Language Selection**: Choose your preferred language from the start screen.
2. **Input Your Data**:
   - Gender (Male/Female)
   - Age
   - Additional info (e.g., lifestyle, allergies, goals)
3. **Generate Diet**:
   - Press "Create Diet" and the AI will generate a complete weekly meal plan.
4. **Ask Questions**:
   - Use the "Ask a Question" feature to clarify or explore your diet further.

---

## 🔐 Gemini API Key Required

To use the application, you **must provide your own Gemini API key**.

### How to set it up:

1. Get your Gemini API key from: [https://makersuite.google.com/app](https://makersuite.google.com/app)
2. Open the file: `config.py`
3. Paste your key inside the `KEY` variable:

```python
# config.py
KEY = "your-gemini-api-key-here"
```
---
## 🖥️ Technologies Used

- **Python 3** – Core language used for the app logic.
- **PyQt5** – GUI framework for building the multi-window desktop interface.
- **Google Gemini** – AI-powered diet generation and Q&A via `google.generativeai`.
- **Markdown formatting** – Used to display structured diet plans with tables.

---

## 🚨 Disclaimer

> This tool is intended for **general wellness guidance** and is **not a substitute for professional medical advice**.  
> Always consult a **doctor or registered dietitian** before starting any new diet.

