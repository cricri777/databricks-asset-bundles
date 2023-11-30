CREATE TABLE IF NOT EXISTS gtfs_landing.stop_times(
    trip_id                string,
    arrival_time           string,
    departure_time         string,
    stop_id                string,
    stop_sequence          string,
    pickup_type            string,
    drop_off_type          string,
    shape_dist_traveled    string,
    timepoint              string,
    platform_track         string,
    landing_date date
)
USING DELTA CLUSTER BY (landing_date)
COMMENT 'https://developers.google.com/transit/gtfs/reference?hl=fr#tripstxt';
