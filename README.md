# CrewAI Prompt Refinement System

This project develops an AI agent system that transforms initial prompts into professional-grade prompts.

## Workflow

1. **Initial Assessment Agent**: Evaluates the initial prompt to identify any deficiencies, Suggests an appropriate prompt engineering framework based on the assessment.
2. **Web Search Agent**: Explores and identifies at least two alternative frameworks from web.
3. **Example Generation Agent**: Creates few-shot examples utilizing the proposed and alternative frameworks.
4. **Finalization Agent**: Synthesizes all gathered information to craft a refined, professional prompt.

This collaborative approach ensures the generation of high-quality prompts tailored to specific needs.

## Usage

### Installation

First, install the required dependencies:

```bash
pip install -r requirements.txt
```

Before running the system, ensure you have configured the .env file with the required API keys.

### Running via Streamlit

To use the system with a Streamlit interface, run the following command in the root folder:

```bash
streamlit run src/ui/screen.py
```

### Running Directly via CrewAI

Alternatively, you can run the CrewAI system directly by manually defining the inputs and executing:

```python

def run():
    inputs = {
        {"prompt": "<user_input>"}
    }
    try:
        return Prompter().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

run()
```

```bash
python src/prompter/main.py
```

### Using Ollama Models

To use Ollama models, simply uncomment the following lines in your configuration file and set up the parameters accordingly:

```python
    #   ollama_llm = LLM(
	# 	model="ollama/gemma2:2b", # the model name
	# 	base_url="http://localhost:11434", # the ollama endpoint
	# 	)

    @agent
	def web_searcher(self) -> Agent:
		return Agent(
			config=self.agents_config['web_searcher'],
			verbose=True,
			tools=[SerperDevTool()],
			# llm=self.ollama_llm
		)
```

![](docs/streamlit.png)
