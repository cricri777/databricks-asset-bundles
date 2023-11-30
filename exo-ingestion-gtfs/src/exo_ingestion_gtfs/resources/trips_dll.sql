CREATE TABLE IF NOT EXISTS gtfs_landing.trips (
    route_id string,
    service_id string,
    trip_id string,
    trip_headsign string,
    trip_short_name string,
    direction_id string,
    block_id string,
    shape_id string,
    wheelchair_accessible string,
    bikes_allowed string,
    landing_date date
)
USING DELTA CLUSTER BY (landing_date)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#tripstxt';