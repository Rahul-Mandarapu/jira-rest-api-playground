-- This table stores error logs associated with JIRA issues for tracking and debugging purposes.
-- Each error log entry is linked to a specific JIRA issue via its jira_id.
-- The table includes:
--   - id: Auto-incrementing primary key for unique identification of each log entry
--   - jira_id: VARCHAR field storing the JIRA issue identifier (required, not null)
--   - error_log: VARCHAR field containing the error message or details (required, not null)
--   - created_at: TIMESTAMP field automatically set to the current time when a record is inserted
-- An index is created on the jira_id column to optimize queries filtering by JIRA issue,
-- improving performance when searching for all errors associated with a particular issue.
CREATE TABLE issue_error_logs (
    id BIGSERIAL PRIMARY KEY,
    jira_id VARCHAR(255) NOT NULL,
    error_log VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_issue_error_logs_jira_id ON issue_error_logs(jira_id);
