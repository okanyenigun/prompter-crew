from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv


load_dotenv()


manager_llm = LLM(model="gpt-4o") 


@CrewBase
class Prompter():

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def first_level_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['first_level_writer'],
			verbose=True
		)

	@task
	def analyze_prompt(self) -> Task:
		return Task(
			config=self.tasks_config['analyze_prompt'],
		)

	@task
	def apply_direction(self) -> Task:
		return Task(
			config=self.tasks_config['apply_direction'],
		)

	@task
	def specify_format(self) -> Task:
		return Task(
			config=self.tasks_config['specify_format'],
		)

	@task
	def provide_examples(self) -> Task:
		return Task(
			config=self.tasks_config['provide_examples'],
		)

	@task
	def finalize_prompt(self) -> Task:
		return Task(
			config=self.tasks_config['finalize_prompt'],
		)

	@crew
	def crew(self) -> Crew:
		return Crew(
			agents=self.agents,
			tasks=self.tasks, 
			process=Process.hierarchical, 
			verbose=True,
			manager_llm=manager_llm,
			output_log_file="crew_operations.log",
		)
