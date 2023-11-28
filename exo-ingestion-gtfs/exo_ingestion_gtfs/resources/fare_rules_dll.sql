CREATE TABLE IF NOT EXISTS gtfs_landing.fare_rules (
    fare_id string,
    route_id string,
    origin_id string,
    destination_id string,
    contains_id string,
    landing_date date
)
USING DELTA CLUSTER BY (landing_date)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#fare_rulestxt';
