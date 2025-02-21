#!/usr/bin/env python
import warnings
from .crew import Prompter

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run(inputs):
    try:
        return Prompter().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")