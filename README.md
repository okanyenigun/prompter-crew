# Prompter Crew

An AI agent system that transforms initial prompts into professional-grade prompts using CrewAI.

## Overview

Prompter Crew is a multi-agent system designed to enhance and optimize prompts for better AI interactions. The system takes basic prompts and transforms them into well-structured, professional prompts that yield better results from AI models.

## Features

- **Multi-Agent Architecture**: Built with CrewAI framework
- **Prompt Optimization**: Transforms simple prompts into professional-grade ones
- **Configurable Workflows**: Support for different purposes and use cases
- **Report Generation**: Automatic logging and result tracking

## Installation

1. Clone the repository:
```bash
git clone https://github.com/okanyenigun/prompter-crew.git
cd prompter-crew
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the prompt enhancement system:

```bash
cd prompter/src/prompter
python main.py
```

The system will process your input prompt and generate an optimized version with detailed reports saved in the `reports/` directory.

## Project Structure

```
prompter-crew/
├── prompter/
│   ├── src/prompter/
│   │   ├── config/          # Agent and task configurations
│   │   ├── tools/           # Custom tools and utilities
│   │   ├── reports/         # Generated reports and logs
│   │   ├── crew.py          # Main crew implementation
│   │   └── main.py          # Entry point
│   └── knowledge/           # Knowledge base and preferences
├── requirements.txt
└── README.md
```

## Dependencies

- CrewAI 0.148.0
- CrewAI Tools 0.55.0
- Undetected ChromeDriver 3.5.5

## License

This project is open source and available under the MIT License.
