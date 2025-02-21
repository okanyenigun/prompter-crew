from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
from .output_models import CriticizeOutput, FraweworkOutput, WebSearcherOutput, FewShotExampleOutput, FinalOutput


load_dotenv()


@CrewBase
class Prompter():
	"""Prompter crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# ollama_llm = LLM(
	# 	model="ollama/gemma2:2b", # the model name
	# 	base_url="http://localhost:11434", # the ollama endpoint
	# 	)

	@agent
	def retainer(self) -> Agent:
		return Agent(
			config=self.agents_config['retainer'],
			verbose=True,
			# llm=self.ollama_llm
		)

	@agent
	def web_searcher(self) -> Agent:
		return Agent(
			config=self.agents_config['web_searcher'],
			verbose=True,
			tools=[SerperDevTool()],
			# llm=self.ollama_llm
		)
	
	@agent
	def exampler(self) -> Agent:
		return Agent(
			config=self.agents_config['exampler'],
			verbose=True,
			# llm=self.ollama_llm
		)
	
	@agent
	def copywriter(self) -> Agent:
		return Agent(
			config=self.agents_config['copywriter'],
			verbose=True,
			# llm=self.ollama_llm
		)

	@task
	def criticize(self) -> Task:
		return Task(
			config=self.tasks_config['criticize'],
			output_pydantic=CriticizeOutput,	
		)

	@task
	def find_framework(self) -> Task:
		return Task(
			config=self.tasks_config['find_framework'],
			context=[self.criticize()],
			output_pydantic=FraweworkOutput,
		)
	
	@task
	def search_for_alternative_frameworks(self) -> Task:
		return Task(
			config=self.tasks_config['search_for_alternative_frameworks'],
			context=[self.find_framework()],
			output_pydantic=WebSearcherOutput
		)
	
	@task
	def create_few_shot_examples(self) -> Task:
		return Task(
			config=self.tasks_config['create_few_shot_examples'],
			context=[self.find_framework(), self.search_for_alternative_frameworks()],
			output_pydantic=FewShotExampleOutput
		)

	@task
	def write_final_prompts(self) -> Task:
		return Task(
			config=self.tasks_config['write_final_prompts'],
			context=[
				self.criticize(),
				self.find_framework(),
				self.search_for_alternative_frameworks(),
				self.create_few_shot_examples()
			],
			output_pydantic=FinalOutput
		)

	@crew
	def crew(self) -> Crew:

		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
			
		)
