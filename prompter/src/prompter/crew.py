import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent
from dotenv import load_dotenv
from datetime import datetime
from tools.scrap import collect_tools_from_hub


load_dotenv()


@CrewBase
class Prompter():

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def prompt_copywriter(self) -> Agent:
		return Agent(
			config=self.agents_config['prompt_copywriter'],
			verbose=True
		)

	@agent
	def hub_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['hub_researcher'],
			tools=[collect_tools_from_hub],
			verbose=True
		)
	
	def create_conditional_crew(self, purpose: str):
		"""Create a crew with tasks selected based on purpose"""
		os.makedirs("reports", exist_ok=True)
		timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
		
		# Get appropriate tasks for the purpose
		selected_tasks = self.get_tasks_for_purpose(purpose)
		
		return Crew(
			agents=[self.prompt_copywriter(), self.hub_researcher()], # Both agents needed for the workflow
			tasks=selected_tasks,
			process=Process.sequential,
			verbose=True,
			output_log_file=f"reports/crew_log_{timestamp}.txt",
		)
	
	def get_tasks_for_purpose(self, purpose: str):
		"""Return the appropriate tasks based on the purpose"""
		timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
		
		if purpose.lower() == "rag":
			# Stage 1: RAG optimization
			rag_task = Task(
				config=self.tasks_config['rag_alignment'],
			)
		elif purpose.lower() == "langchain":
			# Stage 1: LangChain optimization
			langchain_task = Task(
				config=self.tasks_config['langchain_structured_output'],
			)
		else:  # default case
			# Stage 1: Five principles optimization
			principles_task = Task(
				config=self.tasks_config['apply_five_principles'],
			)
		
		# Stage 2: Hub research workflow (always follows stage 1)
		hub_keyword_task = Task(
			config=self.tasks_config['hub_keyword_analysis'],
		)
		
		hub_collection_task = Task(
			config=self.tasks_config['hub_prompt_collection'],
			context=[hub_keyword_task],
		)
		
		hub_analysis_task = Task(
			config=self.tasks_config['hub_improvement_analysis'],
			context=[hub_collection_task],
		)
		
		# Return the complete workflow based on purpose
		if purpose.lower() == "rag":
			return [rag_task, hub_keyword_task, hub_collection_task, hub_analysis_task]
		elif purpose.lower() == "langchain":
			return [langchain_task, hub_keyword_task, hub_collection_task, hub_analysis_task]
		else:  # default case
			return [principles_task, hub_keyword_task, hub_collection_task, hub_analysis_task]