import os
import warnings
from crew import Prompter
from datetime import datetime

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {
        'candidate_prompt': "write a joke",
        "purpose": "default", 
    }

    try:
        # Create reports directory
        os.makedirs("reports", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        crew_instance = Prompter()
        selected_crew = crew_instance.create_conditional_crew(inputs['purpose'])

        result = selected_crew.kickoff(inputs=inputs)
        
        final_report_path = f"reports/final_result_{timestamp}.txt"
        with open(final_report_path, 'w', encoding='utf-8') as f:
            f.write("=== PROMPT ENGINEERING CREW - FINAL RESULT ===\n")
            f.write(f"Execution Time: {datetime.now().isoformat()}\n")
            f.write(f"Input Prompt: {inputs['candidate_prompt']}\n")
            f.write(f"Purpose: {inputs['purpose']}\n")
            f.write("="*60 + "\n\n")
            f.write(str(result))
            f.write(f"\n\n{'='*60}\nExecution completed at {datetime.now().isoformat()}\n")

        print(f"\n✅ Crew execution completed!")
        print(f"📄 Final result saved to: {final_report_path}")

        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == "__main__":
    run()