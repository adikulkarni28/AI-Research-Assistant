
# AI-Powered Multi-Agent Research Assistant

An AI-powered research automation system that uses multiple specialized AI agents to search the web, analyze information, summarize findings, and generate structured research reports.

The project uses Python, Ollama, Gradio, and DuckDuckGo Search to automate the research process through a simple web interface.

---

## 1. Project Overview

Researching a topic manually requires visiting multiple websites, reading lengthy articles, collecting information, analyzing findings, and preparing a final report.

This project automates these activities using three specialized AI agents.

**Agent 1 – Web Research Agent**
- Searches the internet for relevant information.
- Collects website titles, URLs, and descriptions.
- Extracts readable content from web pages where accessible.

**Agent 2 – Summarization Agent**
- Analyzes the collected information.
- Identifies important findings and key facts.
- Generates a concise research summary.
- Identifies evidence gaps and limitations.

**Agent 3 – Report Generation Agent**
- Converts summarized information into a structured research report.
- Generates sections such as abstract, introduction, findings, discussion, and conclusion.
- Includes references and source links.
- Saves the report in Markdown format.

Gradio provides an interactive interface for users to enter research topics and view generated reports.

---

## 2. Problem Statement

Manual research is time-consuming because users must search different websites, collect information, compare findings, summarize content, and prepare reports.

The objective of this project is to develop an AI-powered multi-agent system that automates these tasks and generates structured research reports with references.

---

## 3. Objectives

- Automate web-based research.
- Collect relevant information from multiple sources.
- Summarize information using Large Language Models (LLMs).
- Generate structured research reports.
- Provide source references and links.
- Develop a user-friendly Gradio interface.
- Use locally running AI models through Ollama.

---

## 4. Key Features

- Multi-agent AI architecture.
- Automated web research.
- Information extraction and summarization.
- Local LLM integration using Ollama.
- Automatic research report generation.
- Source links and references.
- Interactive Gradio dashboard.
- Downloadable Markdown reports.
- Configurable AI model.
- Modular and maintainable Python architecture.

---

## 5. System Architecture

```text
              USER
                |
                v
        GRADIO WEB INTERFACE
                |
                v
       AGENT 1: WEB RESEARCH
                |
         DuckDuckGo Search
                |
        Information Collection
                |
                v
      AGENT 2: SUMMARIZATION
                |
          Ollama LLM
                |
        Key Findings Analysis
                |
                v
    AGENT 3: REPORT GENERATION
                |
          Ollama LLM
                |
                v
        FINAL RESEARCH REPORT
                |
                v
        MARKDOWN OUTPUT
                |
                v
          USER DOWNLOAD
```

---

## 6. AI Agents and Their Responsibilities

### Agent 1: Web Research Agent

File: `agents/research_agent.py`

Responsibilities:
- Accepts the research topic.
- Searches DuckDuckGo for relevant web pages.
- Collects titles, URLs, and search snippets.
- Attempts to extract webpage content using BeautifulSoup.
- Passes collected information to the next agent.

### Agent 2: Summarization Agent

File: `agents/summarizer_agent.py`

Responsibilities:
- Receives collected research information.
- Analyzes the content using Ollama.
- Extracts important findings.
- Identifies facts and relevant examples.
- Generates an organized research summary.

### Agent 3: Report Generation Agent

File: `agents/report_agent.py`

Responsibilities:
- Receives the research summary.
- Creates a structured research report.
- Generates introduction, findings, discussion, and conclusion.
- Adds numbered references and source links.
- Saves the generated report.

### Ollama Client

File: `agents/ollama_client.py`

This module connects the Python application to the locally running Ollama API.

It sends prompts to the selected language model and receives AI-generated responses.

---

## 7. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Gradio | Web interface |
| Ollama | Local AI model execution |
| Llama 3.2 | Language model |
| DuckDuckGo | Web search |
| BeautifulSoup | Webpage content extraction |
| Requests | HTTP communication |
| python-dotenv | Environment configuration |
| Markdown | Research report generation |

---

## 8. Project Structure

```text
ai_research_assistant/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── agents/
│   ├── __init__.py
│   ├── ollama_client.py
│   ├── research_agent.py
│   ├── summarizer_agent.py
│   └── report_agent.py
│
└── reports/
```

### File Description

- `app.py` – Main application and Gradio interface.
- `config.py` – Configuration settings.
- `ollama_client.py` – Ollama API connection.
- `research_agent.py` – Web search and information collection.
- `summarizer_agent.py` – Research summarization.
- `report_agent.py` – Report generation and saving.
- `requirements.txt` – Required Python libraries.
- `.env.example` – Example environment variables.
- `README.md` – Project documentation.
- `reports/` – Stores generated research reports.

---

## 9. Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Research-Assistant.git

cd AI-Research-Assistant
```

Alternatively, download the project ZIP and extract it.

### Step 2: Create Virtual Environment

For macOS:

```bash
python3 -m venv venv

source venv/bin/activate
```

For Windows:

```bash
python -m venv venv

venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Install Ollama

Download Ollama:

https://ollama.com/

Download the Llama 3.2 model:

```bash
ollama pull llama3.2
```

Verify installation:

```bash
ollama list
```

### Step 5: Start Ollama

```bash
ollama serve
```

Keep Ollama running while using the application.

### Step 6: Configure Environment

Create the `.env` file:

```bash
cp .env.example .env
```

Default configuration:

```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
REQUEST_TIMEOUT=120
MAX_PAGE_CHARS=5000
```

### Step 7: Run the Application

Open another terminal and execute:

```bash
source venv/bin/activate

python app.py
```

Open the following address in your browser:

```text
http://127.0.0.1:7860
```

---

## 10. How the Application Works

1. User enters a research topic in the Gradio interface.
2. Web Research Agent searches the internet.
3. Relevant website information is collected.
4. Summarization Agent analyzes the collected content using Ollama.
5. Report Generation Agent creates a structured research report.
6. The generated report is displayed in the Gradio interface.
7. User can download the report in Markdown format.

---

## 11. Example Research Topics

The application can research topics such as:

- Applications of Artificial Intelligence in Healthcare.
- Machine Learning in Fraud Detection.
- Generative AI and its Future.
- Artificial Intelligence in Education.
- Cybersecurity and Data Privacy.
- Big Data Analytics.
- AI-Based Recommendation Systems.
- Deep Learning Applications.

Example input:

```text
Applications of Artificial Intelligence in Healthcare
```

---

## 12. Generated Report Structure

The system generates reports with the following sections:

1. Abstract
2. Introduction
3. Research Objectives
4. Key Findings
5. Discussion and Analysis
6. Challenges and Limitations
7. Conclusion
8. References

Generated reports are stored in the `reports/` directory.

---

## 13. Advantages

- Reduces manual research effort.
- Automates information collection.
- Separates research into specialized tasks.
- Uses local AI models.
- Provides an easy-to-use interface.
- Generates structured reports.
- Maintains links to original research sources.

---

## 14. Limitations

- Search results depend on internet connectivity.
- Some websites may block automated content extraction.
- Search snippets may not contain complete information.
- AI-generated summaries may contain errors.
- References should be manually verified.
- The current system uses a sequential workflow rather than distributed agents.

---

## 15. Future Enhancements

The project can be extended with:

1. PDF and DOCX report export.
2. Research history using SQLite.
3. Academic paper search integration.
4. PDF document upload and analysis.
5. Source credibility scoring.
6. Citation verification.
7. Interactive research chatbot.
8. Multi-language report generation.
9. Agent execution monitoring dashboard.
10. Advanced multi-agent collaboration.

---

## 16. Viva Explanation

### What is this project?

This is an AI-powered multi-agent research assistant that automates web research, information summarization, and research report generation.

### How many agents are used?

Three specialized agents:
- Web Research Agent.
- Summarization Agent.
- Report Generation Agent.

### What is Ollama?

Ollama is a tool that allows us to run Large Language Models locally on our computer.

### Why use Gradio?

Gradio provides an interactive web interface that allows users to interact with Python applications through a browser.

### Why use multiple agents?

Each agent has a separate responsibility. This makes the application modular, easier to maintain, and easier to extend.

### What is an LLM?

A Large Language Model is an AI model trained on large amounts of text data to understand and generate human-like language.

### What is the role of DuckDuckGo?

It is used to search the web and collect relevant research sources.

---

## 17. Resume Description

**AI-Powered Multi-Agent Research Assistant**

- Developed an AI-powered research automation system using Python, Ollama, Gradio, and DuckDuckGo Search.
- Implemented three specialized agents for web research, information summarization, and automated report generation.
- Integrated local Large Language Models to analyze collected web content and generate structured research reports.
- Built an interactive Gradio interface for submitting research topics and downloading reports with source references.

---

## 18. Responsible Use

This application is designed for research assistance and educational purposes.

Always verify important findings using the original sources. AI-generated content should not be treated as automatically accurate. Respect website terms of service and copyright when collecting and reusing information.

---

## Author

**Aditya Kulkarni**

BE – Artificial Intelligence and Data Science

SGBIT, Belagavi
