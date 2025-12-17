import logic_handler as lh
from pathlib import Path

## ----------------------------------------------------------------
## USER PROMPT INPUT
## ----------------------------------------------------------------

def get_user_prompt():
    prompt = ""

    bug_report_1 = "Bug Report 1: "
    bug_report_2 = "Bug Report 2: "

    # Retrieve user inputs for bug report 1
    # bug_report_1.join(getInputs(true))

    # Retrieve data for bug report 2
    # bug_report_2.join(getInputs(false))

    prompt = f"{lh.INITIAL_PROMPT} {bug_report_1} {bug_report_2}"
    print(f"\n Using prompt: {prompt}")
    return prompt

## ----------------------------------------------------------------
## TOKEN CONFIGURATION INPUT
## ----------------------------------------------------------------

def get_max_new_tokens():
    max_tokens = 0
    user_input = input("Enter max new tokens: ")
    print(f"\n User input for max new tokens: {user_input}")
    if type(user_input) != str or int(user_input) <= 0:
        print(f" Invalid input. Defaulting to {lh.DEFAULT_MAX_NEW_TOKENS}.")
        max_tokens = lh.DEFAULT_MAX_NEW_TOKENS
    else:
        max_tokens = int(user_input)
    
    print(f"\n Using max new tokens: {max_tokens}")
    return int(max_tokens)

## ----------------------------------------------------------------
## MODEL PATH INPUT
## ----------------------------------------------------------------

def get_model_path():
    path = lh.MODEL_PATH
    print(f"\n Using model at: {path}")
    return path
