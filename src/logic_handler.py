## This file handles the logic behind the interactions with Jira API.
## ----------------------------------------------------------------
## IMPORTS
## ----------------------------------------------------------------
import subprocess
import input_hander as ih
from pathlib import Path

INITIAL_PROMPT = """You are a bug detection assistant. 
Your job is to determine whether or not two bug reports written by humans are refferring to the same or differnt bugs. 
Strictly provide a concise answer of 'SAME' or 'DIFFERENT' with confidence percentage with additional reasoning. 
Example: 'DIFFERENT: 10%' or 'SAME: 87%'. This instruction must be followed exactly for all following inputs."""

DEFAULT_MAX_NEW_TOKENS = 50

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "phi3-mini-4k-q4_k_m.gguf"

## ----------------------------------------------------------------
## CLASS DEFINITIONS
## ----------------------------------------------------------------
class BugReport:
        def __init__(self, summary, description, error_logs):
            self.summary = summary
            self.description = description
            self.error_logs = error_logs

## ----------------------------------------------------------------
## COMPARISON - Sentence Similarity Logic
## ----------------------------------------------------------------

## ----------------------------------------------------------------
## COMPARISON - Polarity Logic
## ----------------------------------------------------------------

## ----------------------------------------------------------------
## COMPARISON - LLM Error logs Logic
## ----------------------------------------------------------------

## ----------------------------------------------------------------
## COMPARISON - FINAL Decision Logic
## ----------------------------------------------------------------

def main():
    # Gets the model's init params
    print("Initializing LLM model run... \n\n\n")
    model_path = ih.get_model_path()
    user_prompt = ih.get_user_prompt()
    max_new_tokens = ih.get_max_new_tokens()
    
    # Constructs command line to run the LLM model
    command = construct_command(model_path, user_prompt, max_new_tokens)
    print(f"\n\n\n Running command: {' '.join(command)}")

    # Runs the model
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)

    return

# Helper to construct command line for LLM model run
def construct_command(model_path, user_prompt, max_new_tokens):
    command = [
        "llama-cli",
        "--model", str(model_path),
        "--prompt", user_prompt,
        "--max-new-tokens", str(max_new_tokens)
    ]
    return command

# Main call
if __name__ == "__main__":
    main()