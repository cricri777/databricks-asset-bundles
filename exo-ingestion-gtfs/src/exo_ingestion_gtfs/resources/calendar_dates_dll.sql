CREATE TABLE IF NOT EXISTS gtfs_landing.calendar_dates (
    service_id string,
    date string,
    exception_type string,
    landing_date date
)
USING DELTA CLUSTER BY (landing_date)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#calendar_datestxt';