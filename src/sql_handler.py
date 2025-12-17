## This code handles to pushing and getting from the local SQL database.
## ----------------------------------------------------------------
## IMPORTS
## ----------------------------------------------------------------
import psycopg2
from psycopg2.extras import RealDictCursor
from typing import List, Dict, Any

## ----------------------------------------------------------------
## GET FUNCTIONS - Database Retrieval
## ----------------------------------------------------------------
def get_logs_by_jira_id(conn, jira_id: str) -> List[Dict[str, Any]]:
    """Retrieve all error logs for a specific JIRA issue."""
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(
            "SELECT id, jira_id, error_log, created_at FROM issue_error_logs WHERE jira_id = %s ORDER BY created_at DESC",
            (jira_id,)
        )
        return cur.fetchall()

def get_logs_by_id(conn, log_id: int) -> Dict[str, Any]:
    """Retrieve a specific error log by ID."""
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(
            "SELECT id, jira_id, error_log, created_at FROM issue_error_logs WHERE id = %s",
            (log_id,)
        )
        return cur.fetchone()

def get_all_logs(conn, limit: int = 100) -> List[Dict[str, Any]]:
    """Retrieve all error logs with optional limit."""
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute(
            "SELECT id, jira_id, error_log, created_at FROM issue_error_logs ORDER BY created_at DESC LIMIT %s",
            (limit,)
        )
        return cur.fetchall()

## ----------------------------------------------------------------
## PUT FUNCTIONS - Database Update
## ----------------------------------------------------------------