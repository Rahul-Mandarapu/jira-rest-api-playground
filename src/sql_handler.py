## This code handles to pushing and getting from the local SQL database.
## ----------------------------------------------------------------
## IMPORTS
## ----------------------------------------------------------------
import sqlite3
from typing import List, Dict, Any, Optional
from datetime import datetime

## ----------------------------------------------------------------
## GET FUNCTIONS - Database Retrieval
## ----------------------------------------------------------------
def get_issue_from_queue(issue_id: int) -> Optional[Dict[str, Any]]:
    """Retrieve a single Jira issue from the queue by ID."""
    conn = sqlite3.connect('issues.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM jira_issue_queue WHERE id = ?', (issue_id,))
    row = cursor.fetchone()
    conn.close()
    
    return dict(row) if row else None


def get_error_logs_by_issue(issue_id: int) -> List[Dict[str, Any]]:
    """Retrieve all error logs for a specific issue."""
    conn = sqlite3.connect('issues.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM issue_error_logs WHERE issue_id = ? ORDER BY created_at DESC', (issue_id,))
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]


def is_database_empty() -> bool:
    """Check if the jira_issue_queue table is empty."""
    conn = sqlite3.connect('issues.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM jira_issue_queue')
    count = cursor.fetchone()[0]
    conn.close()
    
    return count == 0

## ----------------------------------------------------------------
## PUT FUNCTIONS - Database Update
## ----------------------------------------------------------------