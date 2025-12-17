## This file handles get requests and post/put requests to Jira API.
## ----------------------------------------------------------------
## IMPORTS
## ----------------------------------------------------------------
import requests 
import auth as au
from typing import Dict, Any

## ----------------------------------------------------------------
## AUTHENTICATION CONSTANTS
## ----------------------------------------------------------------
USER_AUTH = (au.JIRA_USERNAME, au.JIRA_API_TOKEN)
JIRA_URL = au.JIRA_URL

## ----------------------------------------------------------------
## GET FUNCTIONS - Ticket Retrieval
## ----------------------------------------------------------------
def get_jira_issue(issue_key: str) -> Dict[str, Any]:

    """
    Retrieve a Jira issue by its key.
    
    Args:
        jira_url: Base URL of the Jira instance
        issue_key: The issue key (e.g., 'PROJ-123')
        auth: Tuple of (username, api_token) for authentication
    
    Returns:
        Dictionary containing the issue details
    """
    endpoint = f"{JIRA_URL}/rest/api/3/issues/{issue_key}"
    headers = {"Accept": "application/json"}
    
    response = requests.get(endpoint, headers=headers, auth=USER_AUTH)
    response.raise_for_status()
    
    return response.json()

## ----------------------------------------------------------------
## POST FUNCTIONS - Ticket Creation
## ----------------------------------------------------------------

## ----------------------------------------------------------------
## PUT FUNCTIONS - Ticket Update/ Comment Addition
## ----------------------------------------------------------------