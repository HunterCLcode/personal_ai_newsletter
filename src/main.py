#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import AiResearchCrew
from notion import create_page

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'current_time': str(datetime.now())
    }

    try:
        return AiResearchCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    result = run()
    create_page("AI Research Report", result.raw)