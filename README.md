# Startup Incubator Simulator (Freestyle Track)

**Track:** Freestyle  
**Agent Type:** Multi-agent Startup Simulator  
**Language:** Python (ADK-Python)  
**Model:** Gemini 2.0 Flash Exp (Google AI)  
**Submitted by:** Dheeraj Voleti, Mounika Ravva
---

## 1️⃣ Project OverviewLet

The **Startup Incubator Simulator** is a multi-agent system designed to simulate the process of evaluating, developing, and pitching a startup idea.  
It leverages a combination of parallel and sequential agents, long-running tools, and memory systems to emulate a real-world incubator environment.  

**Use Case:** Aspiring founders can quickly explore market potential, product strategy, financial modeling, and investor insights for new startup ideas.  

---

## 2️⃣ Problem Statement

Starting a new venture requires analyzing multiple domains simultaneously:

- Market opportunity (TAM/SAM/SOM)  
- Product roadmap and MVP strategy  
- Investor sentiment and funding potential  
- Technical feasibility and architecture  
- Financial projections  

Manually performing these analyses is **time-consuming** and often inconsistent.

**Solution:** A multi-agent system that automates these evaluations, produces a comprehensive report, and generates a professional pitch deck.  

---

## 3️⃣ Architecture Overview

```text
+---------------------------+
|       Startup Idea        |
+-----------+---------------+
            |
            v
+---------------------------+
|  Parallel Expert Agents   |
|  - Market Analyst Agent   |
|  - Product Manager Agent  |
|  - VC Investor Agent      |
|  - Technical Architect    |
|  - Financial Model Agent  |
+-----------+---------------+
            |
            v
+---------------------------+
|   Report Compilation      |
+-----------+---------------+
            |
            v
+---------------------------+
|  Pitch Deck Generator     |
|  (Long-Running Tool)      |
+-----------+---------------+
            |
            v
+---------------------------+
| Context Compactor Agent   |
+---------------------------+
            |
            v
+---------------------------+
| Final Output & Summary    |
+---------------------------+
```

**Highlights:**

- **Parallel Agents:** Run multiple expert agents simultaneously
- **Memory System:** Session memory + long-term memory + context compaction
- **Observability:** Logging, metrics, and tracing integrated
- **Long-Running Tools:** Pitch deck generated incrementally

---

## 4️⃣ Agent Descriptions

| Agent Name | Role | Output |
|------------|------|--------|
| Market Analyst Agent | Estimates TAM/SAM/SOM | Market size report |
| Product Manager Agent | Product roadmap and SWOT | SWOT and roadmap |
| VC Investor Agent | Investor sentiment evaluation | Funding likelihood & insights |
| Technical Architect Agent | Technical feasibility | Suggested architecture |
| Financial Model Agent | Financial projections | 3-year revenue, cost, profit model |
| Context Compactor Agent | Summarizes old memory | Compact VC thesis summaries |

---

## 5️⃣ Tools Used

- **Custom Tools:** TAM/SAM/SOM, SWOT, Competitor Lookup, Financial Model
- **MCP Tool Integration:** Simulated competitor search
- **Long-Running Tool:** Pitch Deck Generator (slide-by-slide)

---

## 6️⃣ Memory System

- **Session Memory:** Temporary per-session storage
- **Long-Term Memory:** Persistent storage across startup ideas
- **Context Compaction:** Summarizes old memory to prevent token explosion

---

## 7️⃣ Observability

- **Logging:** Tracks agent actions and tool usage
- **Metrics:** Measures execution time and tool call counts
- **Tracing:** Captures agent execution sequences and durations

---

## 8️⃣ Execution Instructions

### Quick Start

```bash
# Clone the repository
git clone https://github.com/ravvamounika/startup-incubator-simulator.git
cd startup-incubator-simulator

# Install dependencies
pip install -r requirements.txt

# Set your Gemini API key
export GEMINI_API_KEY="your_api_key_here"

# Run the simulator
python app.py
```

### Get Your API Key
Get a free Gemini API key at: https://aistudio.google.com/app/apikey

### Expected Output
```
[INFO] 2025-12-01 - [IncubatorSimulator] Launching parallel expert agents...
[INFO] 2025-12-01 - [Market Analyst] Starting market evaluation.
[INFO] 2025-12-01 - [Product Manager] Creating product roadmap...
[INFO] 2025-12-01 - [VC Investor] Evaluating funding potential...
[INFO] 2025-12-01 - [Technical Architect] Assessing architecture...
[INFO] 2025-12-01 - [Financial Model] Generating projections...
[INFO] 2025-12-01 - [IncubatorSimulator] Parallel agents finished in 2.34s
[INFO] 2025-12-01 - [IncubatorSimulator] Generating pitch deck...
[INFO] 2025-12-01 - [IncubatorSimulator] Simulation complete!

=== Simulation Summary ===
Startup Idea: AI-Powered Personal Health Assistant
Agent Outputs: 5 agents completed
Pitch Deck Slides: 10
Context Compaction Summary: Summarized past VC analyses
```

---

## 9️⃣ Technologies Used

- **Framework:** ADK-Python (Agent Development Kit)
- **AI Model:** Gemini 2.0 Flash Exp
- **Language:** Python 3.9+
- **Async:** asyncio for parallel agent execution
- **Observability:** Custom logging, metrics, and tracing middleware

---
