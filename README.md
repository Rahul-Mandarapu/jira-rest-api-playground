# jira-rest-api-playground

## *** DOWNLOADING LLM ****

Currently using Phi-3-mini-4k-instruct.

Locally, the gguf files (same ones in the .gitignore) are stored inside ./models/Phi-3-mini-4k-instruct

The handlers use the relative path to that directory to call the LLM


## *** AUTHENTICATION ***

Within the src directory:

Create a file named "auth.py" with the fields;

1. JIRA_USERNAME = (Your username/email)
2. JIRA_URL = (URL of the site)
3. JIRA_API_TOKEN = (API token used to link your code to jira)

Since this contains sensitive information, make sure that the .gitignore file has "src/auth.py" to prevent exposure and automatic revoking of the token.