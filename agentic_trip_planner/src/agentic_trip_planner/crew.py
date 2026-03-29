from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, task, crew
from crewai.agents.agent_builder.base_agent import BaseAgent

from dotenv import load_dotenv

# tools
from agentic_trip_planner.tools.tavily_tool import search_web
from agentic_trip_planner.tools.currency_tool import convert_currency

load_dotenv()


@CrewBase
class AgenticTripPlanner:
    """AI Trip Planner Crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # ---------- AGENTS ----------

    @agent
    def intent_mapper(self):
        return Agent(config=self.agents_config["intent_mapper"], verbose=True)

    @agent
    def researcher(self):
        return Agent(
            config=self.agents_config["researcher"],
            tools=[search_web],
            verbose=True
        )

    @agent
    def destination_expert(self):
        return Agent(config=self.agents_config["destination_expert"], verbose=True)

    @agent
    def weather_agent(self):
        return Agent(config=self.agents_config["weather_agent"], verbose=True)

    @agent
    def budget_agent(self):
        return Agent(
            config=self.agents_config["budget_agent"],
            tools=[convert_currency],  # 🔥 IMPORTANT
            verbose=True
        )

    @agent
    def transport_agent(self):
        return Agent(config=self.agents_config["transport_agent"], verbose=True)

    @agent
    def hotel_agent(self):
        return Agent(config=self.agents_config["hotel_agent"], verbose=True)

    @agent
    def planner(self):
        return Agent(config=self.agents_config["planner"], verbose=True)

    # ---------- TASKS ----------

    @task
    def intent_mapping_task(self):
        return Task(config=self.tasks_config["intent_mapping_task"])

    @task
    def research_task(self):
        return Task(
            config=self.tasks_config["research_task"],
            context=[self.intent_mapping_task()]
        )

    @task
    def destination_task(self):
        return Task(
            config=self.tasks_config["destination_task"],
            context=[self.research_task()]
        )

    @task
    def weather_task(self):
        return Task(
            config=self.tasks_config["weather_task"],
            context=[self.research_task()]
        )

    @task
    def budget_task(self):
        return Task(
            config=self.tasks_config["budget_task"],
            context=[self.intent_mapping_task(), self.research_task()]
        )

    @task
    def transport_task(self):
        return Task(
            config=self.tasks_config["transport_task"],
            context=[self.research_task()]
        )

    @task
    def hotel_task(self):
        return Task(
            config=self.tasks_config["hotel_task"],
            context=[self.research_task()]
        )

    @task
    def planner_task(self):
        return Task(
            config=self.tasks_config["planner_task"],
            # context=[
            #     self.destination_task(),
            #     self.weather_task(),
            #     self.budget_task(),
            #     self.transport_task(),
            #     self.hotel_task()
            # ]
            context=[
                self.research_task(),
                self.budget_task()
            ]
        )
    @task
    def final_output_task(self):
        return Task(
            config=self.tasks_config["final_output_task"],
            context=[
                self.destination_task(),
                self.weather_task(),
                self.budget_task(),
                self.transport_task(),
                self.hotel_task(),
                self.planner_task()
            ]
        )


    # ---------- CREW ----------

    @crew
    def crew(self):
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )


# ---------- RUN ----------
def run_crew(inputs):
    return AgenticTripPlanner().crew().kickoff(inputs=inputs)