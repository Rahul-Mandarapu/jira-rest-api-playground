import logic_handler as lh
from pathlib import Path

## ----------------------------------------------------------------
## USER PROMPT INPUT
## ----------------------------------------------------------------

def get_user_prompt():
    # Prompt user for bug report details
    bug_report_1 = "Bug Report 1: "
    bug_report_2 = "Bug Report 2: "
    
    # Retrieve user inputs for bug report 1
    print("\n  Enter details for Bug Report 1:")

    selection = input(" 1. Placeholder Bug Report (login error) \n 2. Manual Entry \n Selection: ")

    if selection == "1":
        summary_1 = "Page crashes on login"
        description_1 = "1. Navigate to login on webpage. 2. Attempt login with valid credentials. Expected: Redirected to the homepage. Actual: Crashes with a 500 error."
        error_logs_1 = "Error 500: Internal Server Error."
    else:
        summary_1 = input("\n Summary: ")
        description_1 = input("\n Description: ")
        error_logs_1 = input("\n Error Logs: ")
    bug_report_1 += f"Summary: {summary_1}\n Description: {description_1}\n Error Logs: {error_logs_1}"
    
    # Retrieve data for bug report 2 - PLACEHOLDER FOR SQL AND JIRA INTEGRATION
    print("\n  Select Bug Report 2 (placeholder for SQL and JIRA integration):")
    selection = input(" 1. Duplicate Bug \n 2. Different Bug (login error) \n 3. Edge case (near duplicate) \n 4. Edge case (completely different) \n 5. Edge case (empty fields) \n Selection: ")

    if selection == "1":
        summary_2 = summary_1
        description_2 = description_1
        error_logs_2 = error_logs_1
    elif selection == "2":
        summary_2 = "Page crashes on login"
        description_2 = "1. Navigate to login on webpage. 2. Attempt login with valid credentials. Expected: Redirected to the homepage. Actual: Crashes with a 500 error."
        error_logs_2 = "Error 500: Internal Server Error."
    elif selection == "3":
        summary_2 = summary_1 + " - intermittent"
        description_2 = description_1 + " This issue occurs intermittently under high load."
        error_logs_2 = "Error 502: Bad Gateway."
    elif selection == "4":
        summary_2 = "SCP-2774 Keter Class Object"
        description_2 = "Colloquially known as 'The Slow-burn Sloth', SCP-2774 is a Keter class memetic image that after exposure causes individual's sweat glands to secrete highly corrosive acid."
        error_logs_2 = "Error 2774: Page corroded by anomalous corrosive substance."
    else:
        if selection != "5":
            print("Invalid selection. Defaulting to empty fields.")
        summary_2 = ""
        description_2 = ""
        error_logs_2 = ""

    bug_report_2 += f"Summary: {summary_2}\n Description: {description_2}\n Error Logs: {error_logs_2}"
    # Build final prompt
    prompt = f"{lh.INITIAL_PROMPT} {bug_report_1} {bug_report_2}"

    # Confirm Input
    print(f"\n Using prompt: \n{lh.INITIAL_PROMPT} \n{bug_report_1} \n{bug_report_2} \n")
    return prompt

## ----------------------------------------------------------------
## TOKEN CONFIGURATION INPUT
## ----------------------------------------------------------------

def get_max_new_tokens():
    # Prompt user for max new tokens
    max_tokens = 0
    user_input = input("Enter max new tokens: ")

    # Validate input
    if type(user_input) != str or int(user_input) <= 0:
        print(f" Invalid input. Defaulting to {lh.DEFAULT_MAX_NEW_TOKENS}.")
        max_tokens = lh.DEFAULT_MAX_NEW_TOKENS
    else:
        max_tokens = int(user_input)
    
    # Confirm Input
    print(f"\nUsing max new tokens: {max_tokens}")
    return int(max_tokens)

## ----------------------------------------------------------------
## MODEL PATH INPUT
## ----------------------------------------------------------------

def get_model_path():
    path = lh.MODEL_PATH
    print(f"\n Using model at: {path}")
    return path
