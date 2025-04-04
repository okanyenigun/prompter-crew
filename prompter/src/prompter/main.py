import warnings
from crew import Prompter

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {
        'prompt': 'Create social media content for a fitness app',
    }
    
    try:
        response = Prompter().crew().kickoff(inputs=inputs)
        return response
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

response = run()

print("****************")
print(response)
print("****************")