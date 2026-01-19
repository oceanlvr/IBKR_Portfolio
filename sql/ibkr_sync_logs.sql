CREATE TABLE IF NOT EXISTS ibkr_sync_logs (
    reference_code TEXT PRIMARY KEY,
    query_id TEXT,
    status TEXT, -- 'PENDING', 'SUCCESS', 'ERROR'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


