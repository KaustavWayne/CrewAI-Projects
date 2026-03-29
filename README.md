# AgenticTripPlanner Crew

# ✅ CrewAI Setup (Using venv INSIDE Project)

## 🚀 Step-by-Step Setup

### 1️⃣ Go to project folder
cd D:\CAMPUSX\CrewAI\Project

### 2️⃣ Create CrewAI project
crewai create crew agentic-trip-planner

### 3️⃣ Enter project folder (IMPORTANT: underscore `_`)
cd agentic_trip_planner

### 4️⃣ Create virtual environment INSIDE project
uv venv --python 3.11

### 5️⃣ Activate virtual environment
.venv\Scripts\activate

### 6️⃣ Install CrewAI (choose ONE)
pip install crewai
# OR
uv pip install crewai

OR,
uv pip install -r requirements.txt

### 7️⃣ Install project dependencies
crewai install if you remove crewai[tools] from dependencies in pyproject.toml
try to remove default crewai[tools] from dependencies

### 8️⃣ Run your project
crewai run


---

## ⚠️ Important Notes

- Folder name is:
  agentic_trip_planner (NOT agentic-trip-planner)

- Always activate `.venv` before installing or running anything

- DO NOT use:
  uv tool install crewai ❌ (installs globally, not inside project)

- If `crewai` command doesn’t work:
  python -m crewai run


---

## 🧠 Command Summary

| Command | Use |
|--------|-----|
| pip install crewai | Install inside venv ✅ |
| uv pip install crewai | Faster pip alternative ✅ |
| crewai install | Install project dependencies ✅ |
| crewai run | Run your agents ✅ |
| uv tool install crewai | Global install ❌ avoid |


---

## 🎯 Final Flow

cd agentic_trip_planner  
.venv\Scripts\activate  
pip install crewai  
crewai install  
crewai run  