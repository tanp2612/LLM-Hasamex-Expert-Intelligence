# Hasamex Enterprise Intelligence Platform

An executive-level **Retrieval-Augmented Generation (RAG)** application for analyzing and synthesizing insights from multiple expert interviews in the **European robotic surgery market**.

The platform enables users to ask market-level questions across expert transcripts and receive **evidence-backed answers with source attribution, timestamps, and verbatim supporting quotes**.

🌐 **Live Demo:** [View Deployed App](https://your-streamlit-app-url.streamlit.app)

---

## 🚀 Key Features

### 🔍 Multi-Transcript Intelligence

* Queries multiple expert interviews simultaneously.
* Identifies **cross-market themes, patterns, agreements, and disagreements**.
* Synthesizes information into concise, executive-ready responses.

### 📌 Strict Source Attribution

* Every generated insight is tied back to its source transcript.
* Uses structured citations such as:

  ```text
  [Expert Name - Timestamp]
  ```
* Includes **verbatim supporting quotes** to make findings traceable and auditable.

### 🛡️ Hallucination Guardrails

* Uses prompt-based context validation to restrict responses to available transcript evidence.
* Uses deterministic generation with:

  ```text
  temperature = 0.0
  ```
* Designed to prioritize **grounded responses over unsupported assumptions**.

### 💼 Executive-Focused Interface

* Built with Streamlit for a lightweight interactive experience.
* Custom branding and responsive UI.
* Light/dark mode adaptation.
* Custom avatars and visual elements.
* One-click prompt suggestions for common executive research questions.

---

## 🏗️ How It Works

```text
Expert Interview Transcripts
            ↓
     Document Processing
            ↓
     Context Retrieval
            ↓
   LangChain Prompt Layer
            ↓
      Groq LLM Engine
            ↓
 Evidence-Backed Response
            ↓
Citations + Verbatim Quotes
```

The system takes expert interview transcripts as its knowledge source, retrieves relevant context for a user's question, and passes that context through a structured LangChain prompt before generating the final response.

---

## 🛠️ Tech Stack

| Component             | Technology            |
| --------------------- | --------------------- |
| **Frontend / UI**     | Streamlit             |
| **LLM Orchestration** | LangChain             |
| **Prompt Management** | `ChatPromptTemplate`  |
| **LLM Engine**        | Groq                  |
| **Model**             | `openai/gpt-oss-120b` |
| **Language**          | Python                |
| **Configuration**     | `.env`                |

---

## 📂 Project Structure

```text
hasamex-case-study/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
│
├── data/
│   └── transcripts/
│
└── README.md
```
---

## 📦 Getting Started

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd hasamex-case-study
```

### 2. Install Dependencies

Create a virtual environment if desired:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_actual_groq_api_key_here
```

Make sure `.env` is included in `.gitignore`:

```text
.env
venv/
__pycache__/
```

### 4. Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will be available locally at:

```text
http://localhost:8501
```

---

## ☁️ Deployment

The application can be deployed using **Streamlit Community Cloud**.

### Deployment Steps

1. Push the project to GitHub.
2. Connect the repository to Streamlit Community Cloud.
3. Select `app.py` as the main application file.
4. Add your `GROQ_API_KEY` under the application's secrets/environment configuration.
5. Deploy the application.

Once deployed, the generated Streamlit URL can be added to the **Live Demo** section at the top of this README.

---

## 💡 Example Executive Queries

The platform can be used to investigate questions such as:

* **What are the major adoption barriers for robotic surgery in Europe?**
* **How do experts perceive the competitive landscape?**
* **What factors are influencing hospital purchasing decisions?**
* **Where do experts agree or disagree on market trends?**
* **What unmet needs are repeatedly mentioned across interviews?**
* **Which insights are supported by multiple experts?**

Each response is designed to provide the relevant conclusion along with supporting transcript evidence.

---

## 🎯 Use Case

The platform is designed for **market research and strategic intelligence**, particularly where analysts need to extract structured insights from large volumes of qualitative expert interviews.

Instead of manually reviewing every transcript, users can ask natural-language questions and quickly identify:

* Market trends
* Customer needs
* Adoption barriers
* Competitive insights
* Expert consensus
* Conflicting viewpoints
* Supporting evidence

This makes the analysis process more efficient while maintaining a clear connection between generated insights and their original sources.

---

## 🔐 Security & Best Practices

* Keep API keys in environment variables or Streamlit secrets.
* Never commit `.env` files containing credentials.
* Avoid exposing sensitive interview transcripts publicly.
* Use anonymized expert identifiers when required.
* Validate retrieved context before displaying sensitive information.

---

## 📌 Project Status

**Status:** 🚀 Active Development

The current version focuses on multi-transcript question answering, evidence-based synthesis, source attribution, and an executive-oriented Streamlit interface.

Future improvements may include:

* Advanced transcript chunking and retrieval
* Vector database integration
* Conversation history
* Document upload functionality
* Advanced market analytics
* Exportable executive reports
* Improved citation tracking

---

## 👩‍💻 Author

**Tanvi Prakash Patil**

Built as an enterprise intelligence / RAG case-study project focused on extracting actionable insights from expert market research.