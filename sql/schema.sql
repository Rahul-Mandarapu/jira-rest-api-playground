CREATE TABLE jira_issue_queue (
    id BIGSERIAL PRIMARY KEY,
    project_key TEXT NOT NULL,
    issue_type TEXT NOT NULL,
    summary TEXT NOT NULL,
    description TEXT,
    fields JSONB DEFAULT '{}'::jsonb,
    status TEXT DEFAULT 'pending',
    jira_key TEXT,
    error TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    processed_at TIMESTAMP
);
