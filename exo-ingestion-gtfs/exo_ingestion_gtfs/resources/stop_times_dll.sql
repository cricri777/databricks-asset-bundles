CREATE TABLE IF NOT EXISTS gtfs_landing.stop_times(
    trip_id string,
    arrival_time string,
    departure_time string,
    stop_id string,
    stop_sequence string,
    stop_headsign string,
    pickup_type string,
    drop_off_type string,
    continuous_pickup string,
    continuous_drop_off string,
    shape_dist_traveled string,
    timepoint string,
    landing_date date
)
USING DELTA CLUSTER BY (landing_date)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#tripstxt';
