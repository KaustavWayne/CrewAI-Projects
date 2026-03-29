# 🌍 VoyageAI – AI Trip Planner

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?style=for-the-badge&logo=streamlit)
![CrewAI](https://img.shields.io/badge/CrewAI-Agentic%20AI-purple?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge)
![Gemini](https://img.shields.io/badge/Gemini-AI-blueviolet?style=for-the-badge)
![Tavily](https://img.shields.io/badge/Tavily-Search-green?style=for-the-badge)

---


An **Agentic AI-powered Trip Planner** built using **CrewAI**, designed to generate complete travel plans like a real-world platform (similar to MakeMyTrip).

It intelligently provides:
- 🌤 Weather insights  
- 🏨 Hotel recommendations  
- 💰 Budget breakdown  
- 🚗 Transport options  
- 🗓 Day-wise itinerary  

---

# 🚀 Features

- 🤖 Multi-Agent System (CrewAI)
- 🔍 Smart Travel Research (Tavily API)
- 💱 Currency Conversion Tool
- 📊 Structured Budget Planning
- 🧭 Day-wise Itinerary (Morning / Afternoon / Evening)
- 🎨 Modern Streamlit UI
- 🧱 JSON-based Architecture (Production-style)

---

# 🏗️ Architecture

```text
User Input → Intent Mapper → Research Agent → Specialized Agents
(destination, weather, budget, hotels, transport)
→ Planner → Final Output → Streamlit UI
```

## 🧠 Agents Used

- 🧭 Intent Mapper – Understands user query
- 🔎 Researcher – Fetches travel data
- 🌍 Destination Expert – Overview & highlights
- 🌤 Weather Agent – Travel weather insights
- 💰 Budget Agent – Cost breakdown
- 🏨 Hotel Agent – Stay recommendations
- 🚗 Transport Agent – Travel options
- 🧠 Planner – Day-wise itinerary

---

# 🛠️ Tech Stack

- Python
- CrewAI
- Streamlit
- Groq / Gemini (LLM)
- Tavily API
- YAML / JSON Config
- Environment Variables (.env)

---

# 📸 UI Preview

## 🔹 Dashboard

[PLACE DASHBOARD SCREENSHOT HERE]

## 🔹 Budget Breakdown

[PLACE BUDGET SCREENSHOT HERE]

## 🔹 Hotels & Transport

[PLACE HOTELS AND TRANSPORT SCREENSHOT HERE]

---

# 🎥 Demo (Coming Soon)

🔥 I will add a full demo GIF here soon

[PLACE YOUR DEMO GIF HERE]

---

# ⚙️ How It Works

1. User enters trip details
2. Intent Agent extracts structured data
3. Research Agent gathers travel info
4. Specialized agents process:
   - Hotels
   - Budget
   - Weather
   - Transport
5. Planner creates itinerary
6. Final output rendered in UI

---

# 📂 Project Structure

```text
agentic_trip_planner/
│
├── config/
│   ├── agents.yaml
│   ├── tasks.yaml
│
├── tools/
│   ├── tavily_tool.py
│   ├── currency_tool.py
│
├── crew.py
├── main.py
```

> `main.py` powers the Streamlit UI

---

# 🔐 Environment Variables

Create a `.env` file:

```env
TAVILY_API_KEY=your_key
EXCHANGE_RATE_API_KEY=your_key
```

---

# 💡 Future Improvements

- 🖼️ Hotel Images
- 🗺️ Map Integration
- 💳 Booking Links
- 📄 Export Trip as PDF
- 🤖 Chat-based planner

---

# 👨‍💻 Author

Kaustav Roy Chowdhury

---

© 2026 VoyageAI – AI Trip Planner

---

# ⭐ Support

If you like this project:

- 👉 Star this repository ⭐
- 👉 Share with others 🚀

---

# ✅ CrewAI Setup (Using venv INSIDE Project)

## 🚀 Step-by-Step Setup

### 1️⃣ Go to project folder

```bash
cd D:\CAMPUSX\CrewAI\Project
```

### 2️⃣ Create CrewAI project

```bash
crewai create crew agentic-trip-planner
```

### 3️⃣ Enter project folder (IMPORTANT: underscore `_`)

```bash
cd agentic_trip_planner
```

### 4️⃣ Create virtual environment INSIDE project

```bash
uv venv --python 3.11
```

### 5️⃣ Activate virtual environment

```bash
.venv\Scripts\activate
```

### 6️⃣ Install CrewAI (choose ONE)

```bash
pip install crewai
```

OR

```bash
uv pip install crewai
```

OR

```bash
uv pip install -r requirements.txt
```

### 7️⃣ Install project dependencies

```bash
crewai install
```

> If you remove `crewai[tools]` from dependencies in `pyproject.toml`, try to remove the default `crewai[tools]` entry first.

### 8️⃣ Run your project

```bash
crewai run
```

---

# ⚠️ Important Notes

- Folder name is: `agentic_trip_planner` (**NOT** `agentic-trip-planner`)
- Always activate `.venv` before installing or running anything
- **DO NOT use:**

```bash
uv tool install crewai
```

❌ This installs globally, not inside project

- If `crewai` command doesn’t work, use:

```bash
python -m crewai run
```

---

# 🧠 Command Summary

| Command | Use |
|--------|-----|
| `pip install crewai` | Install inside venv ✅ |
| `uv pip install crewai` | Faster pip alternative ✅ |
| `crewai install` | Install project dependencies ✅ |
| `crewai run` | Run your agents ✅ |
| `uv tool install crewai` | Global install ❌ avoid |

---

# 🎯 Final Flow

```bash
cd agentic_trip_planner
.venv\Scripts\activate
pip install crewai
crewai install
crewai run
```