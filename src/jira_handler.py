## This file handles get requests and post/put requests to Jira API.
## ----------------------------------------------------------------
## IMPORTS
## ----------------------------------------------------------------
import requests
from typing import Dict, Any

## ----------------------------------------------------------------
## GET FUNCTIONS - Ticket Retrieval
## ----------------------------------------------------------------
def get_jira_issue(jira_url: str, issue_key: str, auth: tuple) -> Dict[str, Any]:
    """
    Retrieve a Jira issue by its key.
    
    Args:
        jira_url: Base URL of the Jira instance
        issue_key: The issue key (e.g., 'PROJ-123')
        auth: Tuple of (username, api_token) for authentication
    
    Returns:
        Dictionary containing the issue details
    """
    endpoint = f"{jira_url}/rest/api/3/issues/{issue_key}"
    headers = {"Accept": "application/json"}
    
    response = requests.get(endpoint, headers=headers, auth=auth)
    response.raise_for_status()
    
    return response.json()