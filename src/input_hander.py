import logic_handler as lh

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
    # Placeholder for CLI
    default_max_tokens = lh.DEFAULT_MAX_NEW_TOKENS
    print(f"\n Using max new tokens: {default_max_tokens}")
    return default_max_tokens

## ----------------------------------------------------------------
## MODEL PATH INPUT
## ----------------------------------------------------------------

def get_model_path():
    path = lh.MODEL_PATH
    print(f"\n Using model at: {path}")
    return path
