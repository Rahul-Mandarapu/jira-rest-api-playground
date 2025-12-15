-- TABLE: issue_error_logs
-- PURPOSE: Stores error logs and diagnostic information for failed Jira issue processing
-- 
-- COLUMNS:
--   id              : Unique identifier (auto-incrementing bigint)
--   issue_id        : Foreign key reference to jira_issue_queue(id); cascades on delete
--   error_message   : Text description of the error that occurred
--   error_details   : JSON object containing detailed error context/stack traces (defaults to empty object)
--   log_level       : Severity level of the log entry (defaults to 'ERROR')
--   created_at      : Timestamp when the error was logged (defaults to current time)
--
-- INDEXES:
--   idx_issue_error_logs_issue_id : Optimizes queries filtering by issue_id
--
-- RELATIONSHIPS:
--   - CASCADE DELETE: When a jira_issue_queue record is deleted, all associated error logs are removed
CREATE TABLE issue_error_logs (
    id BIGSERIAL PRIMARY KEY,
    issue_id BIGINT NOT NULL REFERENCES jira_issue_queue(id) ON DELETE CASCADE,
    error_message TEXT NOT NULL,
    error_details JSONB DEFAULT '{}'::jsonb,
    log_level TEXT DEFAULT 'ERROR',
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_issue_error_logs_issue_id ON issue_error_logs(issue_id);