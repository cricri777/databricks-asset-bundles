CREATE TABLE IF NOT EXISTS gtfs_landing.calendar (
    service_id string,
    monday string,
    tuesday string,
    wednesday string,
    thursday string,
    friday string,
    saturday string,
    sunday string,
    start_date string,
    end_date string,
    landing_date date
)
USING DELTA CLUSTER BY (landing_date)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#calendartxt';
