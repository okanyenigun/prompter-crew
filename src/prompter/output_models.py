from pydantic import BaseModel, Field
from typing import List


class Deficiency(BaseModel):
	deficiencies: str = Field(..., description="The deficiency in the input.")
	cause: str = Field(..., description="The cause of the deficiency.")
	solution: str = Field(..., description="The solution to the deficiency.")


class CriticizeOutput(BaseModel):
	"""Output of the criticize task"""
	deficiencies: List[Deficiency]


class FraweworkOutput(BaseModel):
	"""Output of the find_framework task"""
	framework: str = Field(..., description="The name of the framework to use.")
	reason: str = Field(..., description="The reason for choosing the framework.")
	details: str = Field(..., description="Details about the framework.")
	initial_prompt: str = Field(..., description="The initial prompt.")
	deficiencies_summary: str = Field(..., description="A summary of the deficiencies in the input.")


class AlternativeFramework(BaseModel):
	framework: str = Field(..., description="The name of the framework.")
	reason: str = Field(..., description="The reason for choosing the framework.")
	details: str = Field(..., description="Details about the framework.")


class WebSearcherOutput(BaseModel):
	frameworks: List[AlternativeFramework]


class FewShotExample(BaseModel):
	framework: str = Field(..., description="The name of the framework.")
	example: str = Field(..., description="The few-shot example.")


class FewShotExampleOutput(BaseModel):
	examples: List[FewShotExample]


class FinalPrompt(BaseModel):
	prompt: str = Field(..., description="The final prompt.")
	framework: str = Field(..., description="The name of the framework.")


class FinalOutput(BaseModel):
	prompts: List[FinalPrompt]